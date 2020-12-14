from aws_cdk.aws_lambda import Function, Code, Runtime
from aws_cdk.core import Construct
from b_aws_testing_framework.tools.cdk_testing.testing_stack import TestingStack

from b_lambda_layer_common.boto3_version import Boto3Version
from b_lambda_layer_common.layer import Layer


class Infrastructure(TestingStack):
    def __init__(self, scope: Construct):
        super().__init__(scope=scope)

        Function(
            scope=self,
            id=f'{self.global_prefix()}TestingFunction',
            code=Code.from_inline('def handler(*args, **kwargs): return "Hello World!"'),
            handler='index.handler',
            runtime=Runtime.PYTHON_3_6,
            layers=[
                Layer(
                    scope=self,
                    name=f'{self.global_prefix()}TestingLayer',
                    boto3_version=Boto3Version.from_string_version('1.16.35'))
            ]
        )
