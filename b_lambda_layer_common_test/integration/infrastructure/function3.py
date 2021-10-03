from aws_cdk.aws_lambda import Function, Code, Runtime
from aws_cdk.core import Stack
from b_aws_testing_framework.tools.cdk_testing.testing_stack import TestingStack
from b_cfn_lambda_layer.package_version import PackageVersion

from b_lambda_layer_common.layer import Layer


class Function3(Function):
    """
    Function that allows us to check whether dependencies can be installed and custom code can be accessed.
    """
    def __init__(self, scope: Stack):
        super().__init__(
            scope=scope,
            id=f'{TestingStack.global_prefix()}TestingFunction3',
            code=Code.from_inline(
                'import urllib3\n'
                'from jose import jwk, jwt\n'
                'from jose.utils import base64url_decode\n'
                'from b_lambda_layer_common import api_gateway\n'
                'from b_lambda_layer_common import exceptions\n'
                'from b_lambda_layer_common import util\n'
                'from b_lambda_layer_common.ssm.ssm_parameter import SSMParameter\n'
                'import boto3\n'
                'import botocore\n'
                '\n\n'
                'def handler(*args, **kwargs):\n'
                '    SSMParameter("TestSSMParam")\n\n'
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
                    name=f'{TestingStack.global_prefix()}TestingLayer3',
                    dependencies={
                        'python-jose': PackageVersion.from_string_version('3.3.0')
                    }
                )
            ]
        )
