from typing import List, Optional, Dict

from aws_cdk.aws_lambda import Code
from aws_cdk.aws_lambda import LayerVersion, Runtime
from aws_cdk.core import BundlingOptions, AssetHashType, BundlingDockerImage, DockerImage
from aws_cdk.core import Stack
from b_lambda_layer_common.package_version import PackageVersion


class LayerV2(LayerVersion):
    def __init__(
            self,
            scope: Stack,
            name: str,
            dependencies: Optional[Dict[str, PackageVersion]] = None,
            docker_image: DockerImage = None,
    ) -> None:
        """
        Constructor.

        :param scope: Parent CloudFormation stack.
        :param name: Unique name of the layer.
        :param dependencies: A dictionary of dependencies to include in the layer.
            Keys are dependency (package) names.
            Values are dependency (package) version objects.
        :param docker_image: Docker image to use when building code.
        """
        self.__dependencies = dependencies or {}
        self.__docker_image = docker_image

        super().__init__(
            scope=scope,
            id=name,
            code=self.build(),
            compatible_runtimes=self.runtimes()
        )

    def build(self) -> Code:
        """
        Builds a code from source.

        :return: Built code that will be used for creating a Lambda layer.
        """
        install_args = ' '.join([
            self.pip_upgrade_args(),
        ])

        preinstall_command = [
            'mkdir -p /tmp/asset-output/python/'
        ]

        install_command = [
            f'if [ -e /asset-input/python/requirements.txt ]; '
            f'then '
            f'pip install -r /asset-input/python/requirements.txt {install_args} -t /tmp/asset-output/python/; '
            f'fi'
        ]

        # Create install commands for each dependency.
        for key, value in self.__dependencies.items():
            install_command.append(self.create_install_dependency_command(
                dependency=key,
                dependency_version=value,
                install_args=install_args
            ))

        # If we have specified an installation command, we must specify build commands.
        build_command = [
            # Copy.
            'cp -R /tmp/asset-output/. /asset-output/.',
            'cp -R /asset-input/. /asset-output/.',

            # Cleanup.
            'find /asset-output/ -type f -name "*.py[co]" -delete',
            'find /asset-output/ -type d -name "__pycache__" -exec rm -rf {} +',
            'find /asset-output/ -type d -name "*.dist-info" -exec rm -rf {} +',
            'find /asset-output/ -type d -name "*.egg-info" -exec rm -rf {} +',
            'rm -f /asset-output/python/requirements.txt',
            'rm -f /asset-output/python/__init__.py',
            'rm -f /asset-output/__init__.py',

            # Validation.
            'ls -la /asset-output/python/.',
            'find /asset-output/ -type f -print0 | sort -z | xargs -0 sha1sum | sha1sum'
        ] if install_command else []

        # If build command is specified, bundling options should be specified too.
        bundling_options = BundlingOptions(
            image=self.__docker_image or BundlingDockerImage.from_registry('python:3.9'),
            command=[
                'bash', '-c', ' && '.join(preinstall_command + install_command + build_command)
            ]
        ) if build_command else None

        # If bundling options are specified, we must specify asset hash type.
        asset_hash_type = AssetHashType.BUNDLE if bundling_options else None

        code = Code.from_asset(
            self.get_source_path(),
            asset_hash_type=asset_hash_type,
            bundling=bundling_options
        )

        return code

    @staticmethod
    def create_install_dependency_command(
            dependency: str,
            dependency_version: Optional[PackageVersion] = None,
            install_args: Optional[str] = None
    ) -> str:
        """
        Creates a "pip install" command for specific dependency (package).

        :param dependency: Dependency name e.g. 'jwt'.
        :param dependency_version: Dependency version.
        :param install_args: Additional installation arguments for pip.

        :return: Install command as a string.
        """
        version = dependency_version or PackageVersion(version_type=PackageVersion.VersionType.LATEST)
        install_args = install_args or ''

        if version.version_type == PackageVersion.VersionType.LATEST:
            install_args += f' {LayerV2.pip_upgrade_args()}'
            return f'pip install {dependency} {install_args} -t /tmp/asset-output/python/'
        elif version.version_type == PackageVersion.VersionType.SPECIFIC:
            return f'pip install {dependency}=={version.version_string} {install_args} -t /tmp/asset-output/python/'
        elif version.version_type == PackageVersion.VersionType.NONE:
            return ''

        raise ValueError('Unsupported enum value.')

    @staticmethod
    def pip_upgrade_args() -> str:
        """
        Pip upgrade arguments that can be used next to "pip install xxx" command to enforce package upgrade.

        :return: Returns arguments as a string that ensure package upgrade.
        """
        return '--upgrade --upgrade-strategy eager'

    @staticmethod
    def get_source_path() -> str:
        from .source import root
        return root

    @staticmethod
    def runtimes() -> Optional[List[Runtime]]:
        return [
            Runtime.PYTHON_3_6,
            Runtime.PYTHON_3_7,
            Runtime.PYTHON_3_8
        ]
