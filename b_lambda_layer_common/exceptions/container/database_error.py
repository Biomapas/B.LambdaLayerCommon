from typing import Optional

from b_lambda_layer_common.exceptions.http_exception import HttpException


class DatabaseError(HttpException):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message)

    @staticmethod
    def http_code() -> int:
        return 500

    @staticmethod
    def identifier() -> str:
        return 'B_DATABASE_ERROR'

    @staticmethod
    def description() -> str:
        return (
            'The server encountered an unexpected condition that prevented it from fulfilling the request.'
        )
