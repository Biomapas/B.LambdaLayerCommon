from typing import Any, Dict


class ResponseHeaders:
    def __init__(self, headers: Dict[Any, Any]) -> None:
        self.__headers = headers

    @property
    def headers_dict(self):
        return self.__headers

    @staticmethod
    def merge(*headers: 'ResponseHeaders') -> 'ResponseHeaders':
        container = {}

        for head in headers:
            container = {
                **container,
                **head.headers_dict
            }

        return ResponseHeaders(container)

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

    @staticmethod
    def wav_headers() -> 'ResponseHeaders':
        """
        Audio file WAV content type header.
        """
        return ResponseHeaders({
            # Indicate that response is of audio type, wav subtype.
            'Content-Type': 'audio/wav'
        })

    @staticmethod
    def mpeg_headers() -> 'ResponseHeaders':
        """
        Audio file MP3 content type header.
        """
        return ResponseHeaders({
            # Indicate that response is of audio type, mpeg subtype.
            'Content-Type': 'audio/mpeg'
        })

    @staticmethod
    def csv_headers() -> 'ResponseHeaders':
        """
        Text file CSV content type header.
        """
        return ResponseHeaders({
            # Indicate that response is of text type, csv subtype.
            'Content-Type': 'text/csv'
        })

    @staticmethod
    def text_headers() -> 'ResponseHeaders':
        """
        Plaintext file content type header.
        """
        return ResponseHeaders({
            # Indicate that response is plaintext.
            'Content-Type': f'text/plain'
        })

    @staticmethod
    def html_headers(charset: str = 'UTF-8') -> 'ResponseHeaders':
        """
        Text file HTML content type header.
        """
        return ResponseHeaders({
            # Indicate that response is of text type, html subtype.
            'Content-Type': f'text/html; charset={charset}'
        })
