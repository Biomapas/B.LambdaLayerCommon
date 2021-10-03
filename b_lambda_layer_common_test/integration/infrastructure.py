from aws_cdk.aws_lambda import Function, Code, Runtime
from aws_cdk.core import Construct
from b_aws_testing_framework.tools.cdk_testing.testing_stack import TestingStack
from b_cfn_lambda_layer.package_version import PackageVersion

from b_lambda_layer_common.layer import Layer


class Infrastructure(TestingStack):
    LAMBDA_FUNCTION_NAME_KEY = 'LambdaFunctionName'

    def __init__(self, scope: Construct):
        super().__init__(scope=scope)

        function = Function(
            scope=self,
            id=f'{self.global_prefix()}TestingFunction',
            code=Code.from_inline(
                'from b_lambda_layer_common import api_gateway\n'
                'from b_lambda_layer_common import exceptions\n'
                'from b_lambda_layer_common import ssm\n'
                'from b_lambda_layer_common import util\n'
                'import boto3\n'
                'import botocore\n'
                '\n\n'
                'def handler(*args, **kwargs):\n'
                '    return dict(\n'
                '        Boto3Version=boto3.__version__,\n'
                '        BotocoreVersion=botocore.__version__,\n'
                '    )'
                '\n'
            ),
            handler='index.handler',
            runtime=Runtime.PYTHON_3_6,
            layers=[
                Layer(
                    scope=self,
                    name=f'{self.global_prefix()}TestingLayer',
                    dependencies={
                        'boto3': PackageVersion.from_string_version('1.16.35'),
                        'botocore': PackageVersion.from_string_version('1.19.35'),
                    }
                )
            ]
        )

        self.add_output(self.LAMBDA_FUNCTION_NAME_KEY, value=function.function_name)

        # Create another function that is not using boto3.
        Function(
            scope=self,
            id=f'{self.global_prefix()}TestingFunction2',
            code=Code.from_inline('def handler(*args, **kwargs): return 200'),
            handler='index.handler',
            runtime=Runtime.PYTHON_3_6,
            layers=[Layer(scope=self, name=f'{self.global_prefix()}TestingLayer2')]
        )
