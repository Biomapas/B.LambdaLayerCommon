from os.path import dirname, abspath
from typing import Optional, List, Dict

from aws_cdk.aws_lambda import Runtime
from aws_cdk.core import Stack
from b_cfn_lambda_layer.lambda_layer import LambdaLayer
from b_cfn_lambda_layer.package_version import PackageVersion


class Layer(LambdaLayer):
    def __init__(
            self,
            scope: Stack,
            name: str,
            additional_pip_install_args: Optional[str] = None,
            dependencies: Optional[Dict[str, PackageVersion]] = None,
            docker_image: Optional[str] = None,
    ) -> None:
        super().__init__(
            scope,
            name,
            source_path=self.get_source_path(),
            code_runtimes=self.runtimes(),
            additional_pip_install_args=additional_pip_install_args,
            dependencies={
                **(dependencies or {}),
                'pynamodb': PackageVersion.from_string_version('5.2.1'),
                'ordered-set': PackageVersion.from_string_version('4.1.0'),
                'cryptography': PackageVersion.from_string_version('37.0.1')
            },
            # Ensure Python 3.8 matches everywhere.
            docker_image=docker_image or 'python:3.8'
        )

    @staticmethod
    def get_source_path() -> str:
        return dirname(abspath(__file__))

    @staticmethod
    def runtimes() -> Optional[List[Runtime]]:
        return [
            Runtime.PYTHON_3_6,
            Runtime.PYTHON_3_7,
            # Even though this layer supports more python versions,
            # It is recommended to use Python 3.8.
            Runtime.PYTHON_3_8
        ]
