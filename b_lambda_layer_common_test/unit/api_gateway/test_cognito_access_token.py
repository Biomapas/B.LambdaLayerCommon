import json

from b_lambda_layer_common.api_gateway.cognito_access_token import CognitoAccessToken
from . import root


def test_FUNC_username_WITH_dummy_lambda_event_EXPECT_successfully_extracted_username():
    """
    Test that the function can extract username from cognito access (auth) token.

    :return: No return.
    """
    with open(f'{root}/dummy_event.json', 'r') as file:
        dummy_event = json.loads(file.read())

    assert CognitoAccessToken(dummy_event).username == 'unique_user_name'
