from typing import Optional

from b_lambda_layer_common.exceptions.http_exception import HttpException


class MalformedPermissionError(HttpException):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message)

    @staticmethod
    def http_code() -> int:
        return 400

    @staticmethod
    def identifier() -> str:
        return 'B_MALFORMED_PERMISSION'

    @staticmethod
    def description() -> str:
        return (
            'The client provided a malformed permission object which does not exist in the server or can not be '
            'understood by the server.'
        )
