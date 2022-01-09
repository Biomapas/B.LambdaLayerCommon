from aws_cdk.aws_lambda import Function, Code, Runtime
from aws_cdk.core import Stack
from b_aws_testing_framework.tools.cdk_testing.testing_stack import TestingStack

from b_lambda_layer_common.layer import Layer


class Function4(Function):
    """
    Function which allows us to test whether 'skip_invocation' decorator works as expected.
    """
    def __init__(self, scope: Stack):
        super().__init__(
            scope=scope,
            id=f'{TestingStack.global_prefix()}TestingFunction4',
            code=Code.from_inline(
                'from b_lambda_layer_common.util.skip_invocation import skip_invocation\n'
                '\n\n'
                '@skip_invocation(determinator="heartbeat")\n'
                'def handler(event, context):\n'
                '    return event'
            ),
            handler='index.handler',
            # Ensure Python 3.8 matches everywhere.
            runtime=Runtime.PYTHON_3_8,
            layers=[Layer(scope=scope, name=f'{TestingStack.global_prefix()}TestingLayer4')]
        )
