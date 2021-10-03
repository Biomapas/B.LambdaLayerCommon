import json

from b_lambda_layer_common.api_gateway.body import Body
from . import root


def test_FUNC_from_urlencoded_WITH_urlencoded_body_EXPECT_successfully_parsed() -> None:
    """
    Test that the function can successfully parse url encoded body.

    :return: No return.
    """
    with open(f'{root}/dummy_event.json', 'r') as file:
        dummy_event = json.loads(file.read())

    dummy_event['body'] = 'TaskAttributes=%7B%22from_country%22%3A%22LT%22%7D&TaskPriority=0'

    parsed = Body(dummy_event).from_urlencoded()

    assert parsed == {'TaskAttributes': {'from_country': 'LT'}, 'TaskPriority': 0}


def test_FUNC_from_json_WITH_json_serialized_body_EXPECT_successfuly_parsed() -> None:
    """
    Test that the function can successfully parse json serialized body.

    :return: No return.
    """
    with open(f'{root}/dummy_event.json', 'r') as file:
        dummy_event = json.loads(file.read())

    dummy_event['body'] = "{\"email\":\"email@biomapas.com\",\"group_id\":\"abc1\"}"

    parsed = Body(dummy_event).from_json()

    assert parsed == {'email': 'email@biomapas.com', 'group_id': 'abc1'}
