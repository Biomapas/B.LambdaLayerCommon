from typing import Optional

from b_lambda_layer_common.exceptions.http_exception import HttpException


class MisconfiguredError(HttpException):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message)

    @staticmethod
    def http_code() -> int:
        return 500

    @staticmethod
    def identifier() -> str:
        return 'B_MISCONFIGURED'

    @staticmethod
    def description() -> str:
        return (
            'The server encountered an unexpected server configuration (e.g. missing environment variables) that '
            'prevented it from fulfilling the request.'
        )
