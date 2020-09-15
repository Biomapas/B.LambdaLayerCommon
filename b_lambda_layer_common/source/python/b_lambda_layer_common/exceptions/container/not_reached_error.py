import logging
from typing import Optional

logger = logging.getLogger(__name__)

try:
    from b_lambda_layer_common.exceptions.http_exception import HttpException
except ImportError as ex:
    logger.exception(f'Failed import.')
    from b_lambda_layer_common.source.python.b_lambda_layer_common.exceptions.http_exception import HttpException


class NotReachedError(HttpException):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message)

    @staticmethod
    def http_code() -> int:
        return 0

    @staticmethod
    def identifier() -> str:
        return 'B_NOT_REACHED'

    @staticmethod
    def description() -> str:
        return (
            'The server tried to call another server in order to complete the initial request, however, '
            'failed to do so because the host was not reachable.'
        )
