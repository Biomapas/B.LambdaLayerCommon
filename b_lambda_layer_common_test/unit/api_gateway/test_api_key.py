import pytest

from b_lambda_layer_common.api_gateway.api_key import ApiKey
from b_lambda_layer_common.exceptions.container.forbidden_error import ForbiddenError


@pytest.mark.parametrize(
    "event",
    [
        {'api_key': '123', 'private_api': True},
        {'ApiKey': '123', 'private_api': True},
        {'headers': {'api_key': '123'}},
        {'headers': {'ApiKey': '123'}},
        {'requestContext': {'authorizer': {'api_key': '123'}}},
        {'requestContext': {'authorizer': {'ApiKey': '123'}}},
    ]
)
def test_FUNC_api_key_get_WITH_valid_api_key_EXPECT_api_key_extracted(event) -> None:
    """
    Test that the function can successfully parse lambda event and find an api key.

    :return: No return.
    """
    ApiKey(event).get()


@pytest.mark.parametrize(
    "event",
    [
        {'api_key': '123', 'private_api': False},
        {'ApiKey': ['123']},
        {'header': {'api_key': 123}},
        {'headers': {'Api_Key': 123}},
        {'requestContext': {'authorizer': {'api_key': None}}},
        {'requestContext': {'authorizer': {'ApiKey': '123'}}, 'private_api': True},
    ]
)
def test_FUNC_api_key_get_WITH_invalid_api_key_EXPECT_exception_raised(event) -> None:
    """
    Test that the function will raise an error if api key was not found.

    :return: No return.
    """
    with pytest.raises(ForbiddenError):
        ApiKey(event).get()
