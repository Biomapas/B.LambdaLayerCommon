from typing import Optional, List

from aws_cdk.aws_lambda import LayerVersion, Runtime, Code
from aws_cdk.core import Stack

from b_lambda_layer_common.source import root


class Layer(LayerVersion):
    def __init__(self, scope: Stack, name: str):
        self.__scope = scope

        super().__init__(
            scope=scope,
            id=name,
            code=Code.from_asset(root),
            compatible_runtimes=self.runtimes(),
            layer_version_name=name,
        )

    def runtimes(self) -> Optional[List[Runtime]]:
        return [
            Runtime.PYTHON_3_6,
            Runtime.PYTHON_3_7,
            Runtime.PYTHON_3_8
        ]
