import logging
from functools import wraps

from b_lambda_layer_common.api_gateway.response import Response
from b_lambda_layer_common.api_gateway.response_headers import ResponseHeaders
from b_lambda_layer_common.exceptions.container.internal_error import InternalError
from b_lambda_layer_common.exceptions.http_exception import HttpException

logger = logging.getLogger(__name__)

def exception_middleware(func):
    @wraps(func)
    def wrapper_decorator(*args, **kwargs):
        response_headers = ResponseHeaders.merge(
            ResponseHeaders.allow_all_cors_headers(),
            ResponseHeaders.json_headers()
        )

        try:
            return func(*args, **kwargs)
        except HttpException as ex:
            logger.exception('HTTP exception encountered.')

            data = ex.data()

            return Response.json(
                http_status=ex.http_code(),
                headers=response_headers,
                body=data
            )
        except Exception as ex:
            logger.exception('Unexpected exception encountered.')

            error = InternalError(str(ex))

            return Response.json(
                http_status=error.http_code(),
                headers=response_headers,
                body=error.data()
            )

    return wrapper_decorator
