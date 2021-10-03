import json
import logging
import time

import urllib3
from urllib3 import HTTPResponse
from urllib3.exceptions import HTTPError

from b_lambda_layer_common.exceptions.container.internal_error import InternalError
from b_lambda_layer_common.exceptions.container.not_reached_error import NotReachedError
from b_lambda_layer_common.exceptions.exception_mapper import ExceptionMapper

logger = logging.getLogger(__name__)


class HttpCall:
    WAIT_EXPONENTIATION_FACTOR = 2
    MAXIMUM_SINGLE_WAIT = 4
    INITIAL_WAIT_TIME = 0.25

    @staticmethod
    def call(method, url, fields=None, headers=None, **urlopen_kw) -> HTTPResponse:
        """
        Wrapper for urllib3 pool manager request method. The reason why we have a wrapper here
        is to be able to raise custom http exceptions that this library provides.

        :param method: Http method e.g. GET.
        :param url: Endpoint url to call.
        :param fields: Dictionary fields to be serialized to JSON.
        :param headers: Headers for the http call.
        :param urlopen_kw: Additional urllib3 request parameters.

        :return: Http response.
        """
        http = urllib3.PoolManager()

        logger.debug(
            f'Calling endpoint...\n'
            f'{method} {url}\n'
            f'{headers=}\n'
            f'{fields=}\n'
            f'{urlopen_kw=}.'
        )

        wait_length = HttpCall.INITIAL_WAIT_TIME
        last_exception = None
        while wait_length <= HttpCall.MAXIMUM_SINGLE_WAIT:
            try:
                try:
                    response: HTTPResponse = http.request(
                        method=method,
                        url=url,
                        fields=fields,
                        headers=headers,
                        **urlopen_kw
                    )
                except HTTPError as ex:
                    raise NotReachedError(str(ex))
                if HttpCall.is_status_repeatable(response.status):
                    try:
                        error_data = json.loads(response.data)
                        ExceptionMapper.map_and_raise(error_data)
                    except ValueError:
                        raise InternalError(f'Http call failed with status: {response.status}.')
            except Exception as ex:
                # Store the last exception thrown to rethrow at a later point.
                last_exception = ex
                time.sleep(wait_length)
                wait_length *= HttpCall.WAIT_EXPONENTIATION_FACTOR
            else:
                # Successful request.
                if 400 <= response.status <= 599:
                    try:
                        error_data = json.loads(response.data)
                        ExceptionMapper.map_and_raise(error_data)
                    except ValueError:
                        raise InternalError(f'Http call failed with status: {response.status}.')
                return response
        # Retry attempts exceeded, raise the last exception.
        raise last_exception

    @staticmethod
    def is_status_repeatable(status: int):
        # 429 is "Too many requests" and we try to repeat on all 5xx errors.
        return (status == 429 or status >= 500)
