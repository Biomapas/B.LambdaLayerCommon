import json

from b_aws_testing_framework.credentials import Credentials
from botocore.response import StreamingBody

from b_lambda_layer_common_test.integration.infrastructure.main_stack import MainStack


def test_RESOURCE_lambda_layer_WITH_deployed_lambda_function_1_EXPECT_execution_successful():
    """
    Test whether the layer provides necessary functionality.

    :return: No return.
    """
    # Create client for lambda service.
    lambda_client = Credentials().boto_session.client('lambda')

    # Invoke specific lambda function.
    response = lambda_client.invoke(
        FunctionName=MainStack.get_output(MainStack.LAMBDA_FUNCTION_1_NAME_KEY),
        InvocationType='RequestResponse'
    )

    # Parse the result.
    payload: StreamingBody = response['Payload']
    data = [item.decode() for item in payload.iter_lines()]
    data = json.loads(''.join(data))

    # Assert that the result is as expected.
    assert data['Boto3Version'] == '1.16.35', data
    assert data['BotocoreVersion'] == '1.19.35', data


def test_RESOURCE_lambda_layer_WITH_deployed_lambda_function_2_EXPECT_execution_successful():
    """
    Test whether the layer provides necessary functionality.

    :return: No return.
    """
    # Create client for lambda service.
    lambda_client = Credentials().boto_session.client('lambda')

    # Invoke specific lambda function.
    response = lambda_client.invoke(
        FunctionName=MainStack.get_output(MainStack.LAMBDA_FUNCTION_2_NAME_KEY),
        InvocationType='RequestResponse'
    )

    # Parse the result.
    payload: StreamingBody = response['Payload']
    data = [item.decode() for item in payload.iter_lines()]

    print(data)


def test_RESOURCE_lambda_layer_WITH_deployed_lambda_function_3_EXPECT_execution_successful():
    """
    Test whether the layer provides necessary functionality.

    :return: No return.
    """
    # Create client for lambda service.
    lambda_client = Credentials().boto_session.client('lambda')

    # Invoke specific lambda function.
    response = lambda_client.invoke(
        FunctionName=MainStack.get_output(MainStack.LAMBDA_FUNCTION_3_NAME_KEY),
        InvocationType='RequestResponse'
    )

    # Parse the result.
    payload: StreamingBody = response['Payload']
    data = [item.decode() for item in payload.iter_lines()]
    data = json.loads(''.join(data))

    # Assert that the result is as expected.
    assert data['Boto3Version']
    assert data['BotocoreVersion']

def test_RESOURCE_lambda_layer_WITH_deployed_lambda_function_4_EXPECT_execution_successful():
    """
    Test whether a layer provides necessary functionality.

    :return: No return.
    """
    # Create client for Lambda service.
    lambda_client = Credentials().boto_session.client('lambda')

    # Invoke a specific lambda function.
    response = lambda_client.invoke(
        FunctionName=MainStack.get_output(MainStack.LAMBDA_FUNCTION_4_NAME_KEY),
        InvocationType='RequestResponse',
        Payload=json.dumps({'heartbeat': True})
    )

    # If Lambda function was not executed, it returns a string 'null'.
    data = response['Payload'].read().decode()
    assert data == 'null'
