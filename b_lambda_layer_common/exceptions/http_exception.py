from abc import ABC
from typing import Optional, Any, Dict

from b_lambda_layer_common.exceptions.b_exception import BException


class HttpException(BException, ABC):
    SERIALIZATION_KEY_CODE = 'code'

    def __init__(self, message: Optional[str] = 'No message'):
        super().__init__(message)

    @staticmethod
    def http_code() -> int:
        raise NotImplementedError()

    def data(self) -> Dict[str, Any]:
        base_data = super().data()
        base_data[self.SERIALIZATION_KEY_CODE] = self.http_code()
        return base_data
