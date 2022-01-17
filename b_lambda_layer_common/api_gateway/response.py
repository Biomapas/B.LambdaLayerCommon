import json
from json import JSONEncoder
from typing import Optional, Dict, Any, Type

from b_lambda_layer_common.api_gateway.response_headers import ResponseHeaders


class Response:
    @staticmethod
    def message(
            status: int,
            message: str,
            headers: Optional[ResponseHeaders] = None,
    ) -> Dict[str, Any]:
        return Response.json(http_status=status, headers=headers, body={'message': message})

    @staticmethod
    def json(
            http_status: int,
            headers: Optional[ResponseHeaders] = None,
            body: Optional[Dict[Any, Any]] = None,
            json_encoder: Optional[Type[JSONEncoder]] = None
    ) -> Dict[Any, Any]:
        r = {
            'isBase64Encoded': False,
            'statusCode': http_status
        }

        if headers is not None:
            r['headers'] = headers.headers_dict

        if body is not None:
            r['body'] = json.dumps(body, cls=json_encoder)

        return r

    @staticmethod
    def media(
            http_status: int,
            headers: ResponseHeaders,
            body: bytes
    ) -> Dict[Any, Any]:
        r = {
            'isBase64Encoded': True,
            'statusCode': http_status,
            'headers': headers.headers_dict,
            'body': body
        }

        return r

    @staticmethod
    def any(
            http_status: int,
            headers: ResponseHeaders,
            body: Any,
            encoded: bool = False,
    ) -> Dict[Any, Any]:
        r = {
            'isBase64Encoded': encoded,
            'statusCode': http_status,
            'body': body
        }
        if headers:
            r['headers'] = headers.headers_dict

        if body:
            r['body'] = body

        return r
