from typing import Optional

from b_lambda_layer_common.exceptions.http_exception import HttpException


class ConflictError(HttpException):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message)

    @staticmethod
    def http_code() -> int:
        return 409

    @staticmethod
    def identifier() -> str:
        return 'B_CONFLICT'

    @staticmethod
    def description() -> str:
        return (
            'The request could not be completed due to a conflict with the current state of the target resource. '
            'This code is used in situations where the user might be able to resolve the conflict and resubmit '
            'the request.'
        )
