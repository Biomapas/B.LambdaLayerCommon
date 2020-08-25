import json

from b_lambda_layer_common.source.python.api_gateway.url import Url
from b_lambda_layer_common_test.api_gateway import root


def test_from_event():
    with open(f'{root}/dummy_event.json', 'r') as file:
        dummy_event = json.loads(file.read())

    assert Url.from_event(dummy_event) == 'https://awsid.execute-api.eu-central-1.amazonaws.com/stage'
