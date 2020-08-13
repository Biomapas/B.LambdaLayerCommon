from typing import Any, Dict


class ResponseHeaders:
    def __init__(self, headers: Dict[Any, Any]) -> None:
        self.__headers = headers

    @property
    def headers_dict(self):
        return self.__headers

    @staticmethod
    def merge(headers1: 'ResponseHeaders', headers2: 'ResponseHeaders') -> 'ResponseHeaders':
        return ResponseHeaders({
            **headers1.headers_dict,
            **headers2.headers_dict
        })

    @staticmethod
    def allow_all_cors_headers() -> 'ResponseHeaders':
        return ResponseHeaders({
            # Required for CORS support to work.
            'Access-Control-Allow-Origin': '*',
            # Required for cookies, authorization headers with HTTPS.
            'Access-Control-Allow-Credentials': True
        })

    @staticmethod
    def json_headers() -> 'ResponseHeaders':
        return ResponseHeaders({
            # Indicate that response is serialized dictionary in JSON format.
            'Content-Type': 'application/json'
        })
