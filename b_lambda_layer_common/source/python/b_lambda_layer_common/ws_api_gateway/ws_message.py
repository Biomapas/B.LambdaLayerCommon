import json
from enum import Enum


class WsMessageType(Enum):
    SUCCESS = 'SUCCESS'
    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'


class WsMessage:
    @staticmethod
    def success(text: str) -> bytes:
        return WsMessage.__form_message(text, WsMessageType.SUCCESS)

    @staticmethod
    def info(text: str) -> bytes:
        return WsMessage.__form_message(text, WsMessageType.INFO)

    @staticmethod
    def warning(text: str) -> bytes:
        return WsMessage.__form_message(text, WsMessageType.WARNING)

    @staticmethod
    def error(text: str) -> bytes:
        return WsMessage.__form_message(text, WsMessageType.ERROR)

    @staticmethod
    def __form_message(text: str, type: WsMessageType) -> bytes:
        return json.dumps({
            'message': text,
            'type': type.value
        }).encode('UTF-8')
