from typing import Optional, List

from aws_cdk.aws_lambda import LayerVersion, Runtime, Code
from aws_cdk.core import Stack, AssetHashType, BundlingOptions, BundlingDockerImage

from b_lambda_layer_common.boto3_version import Boto3Version


class Layer(LayerVersion):
    def __init__(self, scope: Stack, name: str, boto3_version: Optional[Boto3Version] = None):
        boto3_version = boto3_version or Boto3Version.dont_install()

        preinstall_command = ['mkdir -p /tmp/asset-output/python/']
        install_command = []
        build_command = []
        bundling_options = None
        asset_hash_type = None

        if boto3_version.version_type == Boto3Version.Boto3VersionType.LATEST:
            install_command.append(f'pip install boto3 --upgrade --upgrade-strategy eager -t /tmp/asset-output/python/')
        elif boto3_version.version_type == Boto3Version.Boto3VersionType.SPECIFIC:
            install_command.append(f'pip install boto3=={boto3_version.version_string} -t /tmp/asset-output/python/')

        # If we have specified an installation command, we must specify build commands.
        if install_command:
            build_command = [
                # Copy.
                'cp -R /tmp/asset-output/. /asset-output/.',
                'cp -R /asset-input/. /asset-output/.',

                # Cleanup.
                'find /asset-output/ -type f -name "*.py[co]" -delete',
                'find /asset-output/ -type d -name "__pycache__" -exec rm -rf {} +',
                'find /asset-output/ -type d -name "*.dist-info" -exec rm -rf {} +',
                'find /asset-output/ -type d -name "*.egg-info" -exec rm -rf {} +',

                # Validation.
                'ls -la /asset-output/python/.',
                'find /asset-output/ -type f -print0 | sort -z | xargs -0 sha1sum | sha1sum'
            ]

        # If build command is specified, bundling options should be specified too.
        if build_command:
            bundling_options = BundlingOptions(
                image=BundlingDockerImage.from_registry('python:3.9'),
                command=[
                    'bash', '-c', ' && '.join(preinstall_command + install_command + build_command)
                ]
            )

        # If bundling options are specified, we must specify asset hash type.
        if bundling_options:
            asset_hash_type = AssetHashType.BUNDLE

        super().__init__(
            scope=scope,
            id=name,
            layer_version_name=name,
            code=Code.from_asset(
                self.get_source_path(),
                asset_hash_type=asset_hash_type,
                bundling=bundling_options
            ),
            compatible_runtimes=self.runtimes()
        )

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
