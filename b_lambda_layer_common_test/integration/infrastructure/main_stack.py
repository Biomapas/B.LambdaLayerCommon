from aws_cdk.core import Construct
from b_aws_testing_framework.tools.cdk_testing.testing_stack import TestingStack

from b_lambda_layer_common_test.integration.infrastructure.function1 import Function1
from b_lambda_layer_common_test.integration.infrastructure.function2 import Function2
from b_lambda_layer_common_test.integration.infrastructure.function3 import Function3
from b_lambda_layer_common_test.integration.infrastructure.function4 import Function4
from b_lambda_layer_common_test.integration.infrastructure.function_with_unit_tests import FunctionWithUnitTests


class MainStack(TestingStack):
    LAMBDA_FUNCTION_1_NAME_KEY = 'LambdaFunctionName1'
    LAMBDA_FUNCTION_2_NAME_KEY = 'LambdaFunctionName2'
    LAMBDA_FUNCTION_3_NAME_KEY = 'LambdaFunctionName3'
    LAMBDA_FUNCTION_4_NAME_KEY = 'LambdaFunctionName4'

    LAMBDA_FUNCTION_UNIT_TESTS_NAME_KEY = 'LambdaFunctionNameUnitTests'

    def __init__(self, scope: Construct):
        super().__init__(scope=scope)

        self.f1 = Function1(self)
        self.f2 = Function2(self)
        self.f3 = Function3(self)
        self.f4 = Function4(self)

        self.f_unit_tests = FunctionWithUnitTests(self)

        self.add_output(self.LAMBDA_FUNCTION_1_NAME_KEY, value=self.f1.function_name)
        self.add_output(self.LAMBDA_FUNCTION_2_NAME_KEY, value=self.f2.function_name)
        self.add_output(self.LAMBDA_FUNCTION_3_NAME_KEY, value=self.f3.function_name)
        self.add_output(self.LAMBDA_FUNCTION_4_NAME_KEY, value=self.f4.function_name)

        self.add_output(self.LAMBDA_FUNCTION_UNIT_TESTS_NAME_KEY, value=self.f_unit_tests.function_name)
