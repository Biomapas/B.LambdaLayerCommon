from typing import Optional

from b_lambda_layer_common.exceptions.http_exception import HttpException


class AlreadyExistsError(HttpException):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message)

    @staticmethod
    def http_code() -> int:
        return 409

    @staticmethod
    def identifier() -> str:
        return 'B_ALREADY_EXISTS'

    @staticmethod
    def description() -> str:
        return (
            'The server understood the request to create entities. However, the request can not be fulfilled because '
            'there are already existing entities and overriding them is not possible or not preferable. Usually, '
            'when a client gets this type of error, an "update" request should be sent, instead of "create".'
        )
