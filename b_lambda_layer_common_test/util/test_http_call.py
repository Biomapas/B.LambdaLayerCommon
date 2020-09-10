from b_lambda_layer_common.source.python.b_lambda_layer_common.exceptions.container.internal_error import InternalError
from b_lambda_layer_common.source.python.b_lambda_layer_common.exceptions.container.not_reached_error import \
    NotReachedError
from b_lambda_layer_common.source.python.b_lambda_layer_common.util.http_call import HttpCall


def test_FUNC_call_WITH_google_endpoint_EXPECT_call_successful() -> None:
    """
    Check whether the call succeeded.

    :return: No return.
    """
    status = HttpCall.call('GET', 'https://google.com').status
    assert status == 200


def test_FUNC_call_WITH_not_existing_url_EXPECT_not_reached() -> None:
    """
    Check whether the call failed.

    :return: No return.
    """
    try:
        HttpCall.call('GET', 'https://awsid.execute-api.eu-central-1.amazonawsxtest.com/stage/x/1/test')
    except NotReachedError:
        pass
    else:
        raise AssertionError('Expected to fail.')


def test_FUNC_call_WITH_not_existing_endpoint_EXPECT_not_found() -> None:
    """
    Check whether the call failed.

    :return: No return.
    """
    try:
        HttpCall.call('GET', 'https://google.com/not/found/resource/123')
    except InternalError as ex:
        assert str(ex) == 'Http call failed with status: 404.'
    else:
        raise AssertionError('Expected to fail.')
