import json

from b_aws_testing_framework.credentials import Credentials
from botocore.response import StreamingBody

from b_lambda_layer_common_test.integration.infrastructure.main_stack import MainStack


def test_RESOURCE_lambda_layer_WITH_with_unit_tests_EXPECT_execution_successful_tests_pass():
    """
    Test whether the layer provides necessary functionality and unit tests pass.

    :return: No return.
    """
    # Create client for lambda service.
    lambda_client = Credentials().boto_session.client('lambda')

    # Invoke specific lambda function.
    response = lambda_client.invoke(
        FunctionName=MainStack.get_output(MainStack.LAMBDA_FUNCTION_UNIT_TESTS_NAME_KEY),
        InvocationType='RequestResponse'
    )

    # Parse the result.
    payload: StreamingBody = response['Payload']
    data = [item.decode() for item in payload.iter_lines()]
    data = json.loads(''.join(data))

    # Assert that the result is as expected i.e. all unit tests inside lambda function have passed.
    assert data.get('ExitCode') == 0, data
