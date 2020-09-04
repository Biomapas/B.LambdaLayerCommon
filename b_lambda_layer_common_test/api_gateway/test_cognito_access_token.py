import json

from b_lambda_layer_common.source.python.api_gateway.cognito_access_token import CognitoAccessToken
from b_lambda_layer_common_test.api_gateway import root


def test_from_event():
    with open(f'{root}/dummy_event.json', 'r') as file:
        dummy_event = json.loads(file.read())

    assert CognitoAccessToken(dummy_event).username == 'unique_user_name'
