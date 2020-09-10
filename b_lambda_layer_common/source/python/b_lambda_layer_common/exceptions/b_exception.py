from abc import ABC
from typing import Optional, Dict, Any


class BException(Exception, ABC):
    SERIALIZATION_KEY_MESSAGE = 'message'
    SERIALIZATION_KEY_IDENTIFIER = 'identifier'
    SERIALIZATION_KEY_DESCRIPTION = 'description'

    def __init__(self, message: Optional[str] = 'No message'):
        super().__init__(message)

        self.__message = message

    def message(self) -> Optional[str]:
        return self.__message

    @staticmethod
    def identifier() -> str:
        raise NotImplementedError()

    @staticmethod
    def description() -> str:
        raise NotImplementedError()

    def data(self) -> Dict[str, Any]:
        return {
            self.SERIALIZATION_KEY_MESSAGE: self.message(),
            self.SERIALIZATION_KEY_IDENTIFIER: self.identifier(),
            self.SERIALIZATION_KEY_DESCRIPTION: self.description(),
        }
