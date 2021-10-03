from typing import Optional

from b_lambda_layer_common.exceptions.http_exception import HttpException


class UnauthorizedError(HttpException):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message)

    @staticmethod
    def http_code() -> int:
        return 401

    @staticmethod
    def identifier() -> str:
        return 'B_UNAUTHORIZED'

    @staticmethod
    def description() -> str:
        return (
            'The request has not been applied because it lacks valid authentication credentials for the target '
            'resource.'
        )
