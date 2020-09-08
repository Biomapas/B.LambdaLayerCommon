import json
import logging

import urllib3
from urllib3 import HTTPResponse
from urllib3.exceptions import HTTPError

logger = logging.getLogger(__name__)

try:
    # Lambda specific imports.
    from exceptions.container.internal_error import InternalError
    from exceptions.container.not_reached_error import NotReachedError
    from exceptions.exception_mapper import ExceptionMapper
except ImportError as ex:
    logger.warning(f'Unable to import: {repr(ex)}.')

    # Project specific imports.
    from b_lambda_layer_common.source.python.exceptions.container.internal_error import InternalError
    from b_lambda_layer_common.source.python.exceptions.container.not_reached_error import NotReachedError
    from b_lambda_layer_common.source.python.exceptions.exception_mapper import ExceptionMapper


class HttpCall:
    @staticmethod
    def call(method, url, fields=None, headers=None, **urlopen_kw) -> HTTPResponse:
        """
        Wrapper for urllib3 pool manager request method.

        :param method: Http method e.g. GET.
        :param url: Endpoint url to call.
        :param fields: Dictionary fields to be serialized to JSON.
        :param headers: Headers for the http call.
        :param urlopen_kw: Additional urllib3 request parameters.

        :return: Http response.
        """
        http = urllib3.PoolManager()

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

        if 400 <= response.status <= 599:
            try:
                error_data = json.loads(response.data)
                ExceptionMapper.map_and_raise(error_data)
            except ValueError:
                raise InternalError(f'Http call failed with status: {response.status}.')

        return response
