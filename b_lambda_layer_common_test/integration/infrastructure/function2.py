from aws_cdk.aws_lambda import Function, Code, Runtime
from aws_cdk.core import Stack
from b_aws_testing_framework.tools.cdk_testing.testing_stack import TestingStack

from b_lambda_layer_common.layer import Layer


class Function2(Function):
    """
    Function that does not really test anything.
    """
    def __init__(self, scope: Stack):
        super().__init__(
            scope=scope,
            id=f'{TestingStack.global_prefix()}TestingFunction2',
            code=Code.from_inline('def handler(*args, **kwargs): return 200'),
            handler='index.handler',
            runtime=Runtime.PYTHON_3_6,
            layers=[Layer(scope=scope, name=f'{TestingStack.global_prefix()}TestingLayer2')]
        )
