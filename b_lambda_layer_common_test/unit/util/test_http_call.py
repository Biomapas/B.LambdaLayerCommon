import time
from urllib3.exceptions import HTTPError

import pook
import pytest

from b_lambda_layer_common.exceptions.container.internal_error import InternalError
from b_lambda_layer_common.exceptions.container.not_reached_error import NotReachedError
from b_lambda_layer_common.util.http_call import HttpCall


def test_FUNC_call_WITH_responsive_url_EXPECT_call_successful() -> None:
    """
    Check whether the call succeeded.

    :return: No return.
    """
    with pook.use():
        pook.get("https://example.com", status=200)
        status = HttpCall.call('GET', 'https://example.com').status
        assert status == 200

def test_FUNC_call_WITH_not_existing_url_EXPECT_not_reached() -> None:
    """
    Check whether the call failed.

    :return: No return.
    """
    with pook.use():
        mock = pook.get("https://unreachable.com").error(HTTPError()).persist()
        with pytest.raises(NotReachedError):
            HttpCall.call('GET', 'https://unreachable.com')


def test_FUNC_call_WITH_not_existing_endpoint_EXPECT_not_found() -> None:
    """
    Check whether the call failed.

    :return: No return.
    """
    with pook.use():
        pook.get("https://example.com/does-not-exist", status=404)
        with pytest.raises(InternalError, match="Http call failed with status: 404."):
            HttpCall.call('GET', "https://example.com/does-not-exist")

def test_FUNC_call_WITH_network_failures_EXPECT_correct_number_of_retries() -> None:
    """
    Check if the retry logic works correctly.

    :return: No return.
    """
    with pook.use():
        mock = pook.get("https://unreachable.com").error(HTTPError()).times(5)
        with pytest.raises(NotReachedError):
            HttpCall.call('GET', 'https://unreachable.com')
        assert mock.total_matches == 5

def test_FUNC_call_WITH_network_failures_EXPECT_correct_time_waiting() -> None:
    """
    Check if the retry logic works correctly.

    :return: No return.
    """
    with pook.use():
        mock = pook.get("https://unreachable.com").error(HTTPError()).times(5)
        with pytest.raises(NotReachedError):
            start = time.time()
            HttpCall.call('GET', 'https://unreachable.com')
        end = time.time()
        time_taken = end - start
        # HttpCall uses an exponentiation algorithm that should result in about 8 seconds long total wait time.
        assert 7.5 < time_taken < 8.5