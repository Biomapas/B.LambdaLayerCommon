import json

from b_lambda_layer_common.api_gateway.url import Url
from . import root


def test_FUNC_from_event_WITH_dummy_lambda_event_EXPECT_api_gateway_rest_api_url_extracted():
    """
    Test whether the function can extract parent api url from lambda event.

    :return: No return.
    """
    with open(f'{root}/dummy_event.json', 'r') as file:
        dummy_event = json.loads(file.read())

    assert Url.from_event(dummy_event) == 'https://awsid.execute-api.eu-central-1.amazonaws.com/stage'
