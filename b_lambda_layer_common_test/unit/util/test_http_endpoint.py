import pook
from b_lambda_layer_common.util.http_endpoint import HttpEndpoint


def test_FUNC_call_to_str_WITH_google_endpoint_EXPECT_successfull_call() -> None:
    """
    Checks whether the http endpoint call to str sends request and receives a response.

    :return: No return.
    """
    with pook.use():
        pook.get('https://example.com')
        endpoint = HttpEndpoint(
            endpoint_url='https://example.com',
            method='GET',
        )

        endpoint.call_to_str()


def test_FUNC_add_auth_token_WITH_dummy_value_EXPECT_authorization_token_added() -> None:
    """
    Checks if auth token can be added to the headers.

    :return: No return.
    """
    endpoint = HttpEndpoint(
        endpoint_url='https://google.com',
        method='GET',
    )

    assert 'Authorization' not in endpoint.headers
    endpoint.add_auth_token('test_token')
    assert endpoint.headers['Authorization'] == 'test_token'
