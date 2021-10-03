from typing import Optional

from b_lambda_layer_common.exceptions.http_exception import HttpException


class NotFoundError(HttpException):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message)

    @staticmethod
    def http_code() -> int:
        return 404

    @staticmethod
    def identifier() -> str:
        return 'B_NOT_FOUND'

    @staticmethod
    def description() -> str:
        return (
            'The origin server did not find a current representation for the target resource or is not willing to '
            'disclose that one exists.'
        )
