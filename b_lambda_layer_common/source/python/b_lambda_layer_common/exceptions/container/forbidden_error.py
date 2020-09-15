import logging
from typing import Optional

logger = logging.getLogger(__name__)

try:
    from b_lambda_layer_common.exceptions.http_exception import HttpException
except ImportError as ex:
    logger.exception(f'Failed import.')
    from b_lambda_layer_common.source.python.b_lambda_layer_common.exceptions.http_exception import HttpException


class ForbiddenError(HttpException):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message)

    @staticmethod
    def http_code() -> int:
        return 403

    @staticmethod
    def identifier() -> str:
        return 'B_FORBIDDEN'

    @staticmethod
    def description() -> str:
        return (
            'The server understood the request but refuses to authorize it. A server that wishes to make public why '
            'the request has been forbidden can describe that reason in the response payload (if any).'
        )
