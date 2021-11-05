from aws_cdk.aws_lambda import Function, Code, Runtime
from aws_cdk.core import Stack, Duration
from b_aws_testing_framework.tools.cdk_testing.testing_stack import TestingStack
from b_cfn_lambda_layer.package_version import PackageVersion

from b_lambda_layer_common.layer import Layer
from b_lambda_layer_common_test.unit import root


class FunctionWithUnitTests(Function):
    """
    Function that lets us run unit tests inside lambda function. We want to run unit
    tests both locally and remotely.
    """
    def __init__(self, scope: Stack):
        super().__init__(
            scope=scope,
            id=f'{TestingStack.global_prefix()}FunctionWithUnitTests',
            code=Code.from_asset(root),
            handler='handler.handler',
            runtime=Runtime.PYTHON_3_8,
            timeout=Duration.minutes(5),
            memory_size=512,
            layers=[
                Layer(
                    scope=scope,
                    name=f'{TestingStack.global_prefix()}TestingLayerWithUnitTests',
                    dependencies={
                        # These dependencies are required for running unit tests inside lambda functions.
                        # Pytest is used for running actual unit tests.
                        'pytest': PackageVersion.from_string_version('6.2.5'),
                        # Pook is used for HTTP mocking, therefore it is also needed here.
                        'pook': PackageVersion.from_string_version('1.0.1'),
                        # Not sure about this dependency. Lambda runtime throws errors if its missing.
                        'aws-cdk.core': PackageVersion.from_string_version('1.99.0'),
                        # This dependency should be installed with 'pook' since it depends on 'jsonschema' which depends on this.
                        # For some reason it doesn't.
                        # Tests would fail with import error otherwise.
                        'importlib-resources': PackageVersion.from_string_version('5.4.0')
                    }
                )
            ]
        )
