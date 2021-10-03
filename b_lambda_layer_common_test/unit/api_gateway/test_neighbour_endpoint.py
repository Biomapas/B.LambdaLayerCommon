import json

from b_lambda_layer_common.api_gateway.neighbour_endpoint import NeighbourEndpoint
from b_lambda_layer_common.exceptions.container.not_reached_error import NotReachedError
from . import root

with open(f'{root}/dummy_event.json', 'r') as file:
    dummy_event = json.loads(file.read())


def test_FUNC_call_WITH_dummy_lambda_event_EXPECT_successfull_call_not_reached_error() -> None:
    """
    Test whether the call was successful with a not reached error.

    :return: No return.
    """
    try:
        NeighbourEndpoint(dummy_event, '/something/', 'GET').call()
    except NotReachedError:
        pass
    else:
        raise AssertionError('Expected to fail.')


def test_FUNC_parent_api_WITH_dummy_lambda_event_EXPECT_parent_api_constructed() -> None:
    """
    Test if parent api was successfully constructed from a lambda event.

    :return: No return.
    """
    endpoint = NeighbourEndpoint(dummy_event, '/test', 'GET')
    assert endpoint.parent_api == 'https://awsid.execute-api.eu-central-1.amazonaws.com/stage'


def test_FUNC_authorization_token_WITH_dummy_lambda_event_EXPECT_token_retrieved() -> None:
    """
    Test whether authorization token was successfully retrieved from lambda event.

    :return: No return.
    """
    endpoint = NeighbourEndpoint(dummy_event, '/test', 'GET')
    assert endpoint.authorization_token == 'Bearer token'


def test_FUNC_full_endpoint_WITH_dummy_lambda_event_and_path_part_EXPECT_successfully_constructed() -> None:
    """
    Test whether the full endpoint to call can be constructed.

    :return: No return.
    """
    endpoint = NeighbourEndpoint(dummy_event, '/test/', 'GET')
    assert endpoint.full_endpoint == 'https://awsid.execute-api.eu-central-1.amazonaws.com/stage/test'
