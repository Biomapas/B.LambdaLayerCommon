from typing import Optional

from b_lambda_layer_common.exceptions.http_exception import HttpException


class BadRequestError(HttpException):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message)

    @staticmethod
    def http_code() -> int:
        return 400

    @staticmethod
    def identifier() -> str:
        return 'B_BAD_REQUEST'

    @staticmethod
    def description() -> str:
        return (
            'The server cannot or will not process the request due to something that is perceived to be a client '
            'error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing).'
        )
