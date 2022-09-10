from typing import Optional

from b_lambda_layer_common.exceptions.http_exception import HttpException


class MalformedValueError(HttpException):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message)

    @staticmethod
    def http_code() -> int:
        return 400

    @staticmethod
    def identifier() -> str:
        return 'B_MALFORMED_VALUE'

    @staticmethod
    def description() -> str:
        return (
            'The client provided a malformed value object which does not conform with '
            'API schema, Database schema or validation procedures.'
        )
