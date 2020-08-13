import json
from typing import Optional, Dict, Any

try:
    from response_headers import ResponseHeaders
except ImportError:
    from b_lambda_layer_common.source.python.api_gateway.response_headers import ResponseHeaders


class Response:
    @staticmethod
    def message(
            status: int,
            message: str,
            headers: Optional[ResponseHeaders],
    ) -> Dict[str, Any]:
        return Response.json(http_status=status, headers=headers, body={'message': message})

    @staticmethod
    def json(
            http_status: int,
            headers: Optional[ResponseHeaders],
            body: Optional[Dict[Any, Any]] = None
    ) -> Dict[Any, Any]:
        r = {
            'isBase64Encoded': False,
            'statusCode': http_status
        }

        if headers:
            r['headers'] = headers.headers_dict

        if body:
            r['body'] = json.dumps(body)

        return r
