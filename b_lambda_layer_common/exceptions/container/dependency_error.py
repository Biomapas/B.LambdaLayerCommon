from typing import Optional

from b_lambda_layer_common.exceptions.http_exception import HttpException


class DependencyError(HttpException):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message)

    @staticmethod
    def http_code() -> int:
        return 424

    @staticmethod
    def identifier() -> str:
        return 'B_FAILED_DEPENDENCY'

    @staticmethod
    def description() -> str:
        return (
            'The method could not be performed on the resource because the requested action depended on another '
            'action and that action failed.'
        )
