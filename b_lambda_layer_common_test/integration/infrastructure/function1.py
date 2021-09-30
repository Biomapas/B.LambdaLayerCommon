from aws_cdk.aws_lambda import Function, Code, Runtime
from aws_cdk.core import Stack
from b_aws_testing_framework.tools.cdk_testing.testing_stack import TestingStack

from b_lambda_layer_common.boto3_version import Boto3Version
from b_lambda_layer_common.layer import Layer
from b_lambda_layer_common.package_version import PackageVersion


class Function1(Function):
    def __init__(self, scope: Stack):
        super().__init__(
            scope=scope,
            id=f'{TestingStack.global_prefix()}TestingFunction1',
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
                    scope=scope,
                    name=f'{TestingStack.global_prefix()}TestingLayer1',
                    boto3_version=Boto3Version.from_string_version('1.16.35'),
                    botocore_version=PackageVersion.from_string_version('1.19.35')
                )
            ]
        )
