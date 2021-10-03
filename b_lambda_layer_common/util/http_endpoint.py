import json
from typing import Optional, Dict, Any, Union, Iterable, AnyStr

from urllib3 import HTTPResponse

from b_lambda_layer_common.util.http_call import HttpCall


class HttpEndpoint:
    """
    Class that represents an http endpoint in OOP way. It is a wrapper class.
    """

    def __init__(
            self,
            endpoint_url: str,
            method: str,
            body: Optional[Union[Dict[Any, Any], Iterable[Any], AnyStr]] = None,
            headers: Optional[Dict[str, str]] = None,
            fields: Optional[Any] = None
    ) -> None:
        """
        Constructor.

        :param endpoint_url: Full endpoint url to call.
        :param method: Http request method type.
        :param body: Body to include in request.
        :param headers: Headers to include in request.
        :param fields: Fields can be one of the following:
            # Regular query parameters or request body { key: value } pairs.
            # Multi-value query parameters [ (key: value1), (key: value2) ] for reused key argument.
            # Filetuple, read more it here: https://urllib3.readthedocs.io/en/latest/reference/urllib3.request.html#urllib3.request.RequestMethods.urlopen
        """
        self.__endpoint_url = endpoint_url
        self.__http_method = method
        self.__http_body = body
        self.__headers = headers or {}
        self.__fields = fields

        assert isinstance(self.__endpoint_url, str), 'Expected string.'
        assert self.__http_method in ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS'], 'Unsupported method.'

    def add_auth_token(self, auth_token: str) -> 'HttpEndpoint':
        """
        Adds an authorization token to headers and returns itself for chaining.

        :param auth_token: Authorization token.

        :return: Itself.
        """
        self.__headers['Authorization'] = auth_token
        return self

    def call_to_json(self) -> Dict[str, Any]:
        """
        Calls a specified endpoint with specified parameters.

        :return: Http response represented as dictionary.
        """
        data = self._call().data

        if data == b'':
            return {}

        return json.loads(data)

    def call_to_bytes(self) -> bytes:
        """
        Calls a specified endpoint with specified parameters.

        :return: Http response represented as bytes.
        """
        return self._call().data

    def call_to_str(self) -> str:
        """
        Calls a specified endpoint with specified parameters.

        :return: Http response represented as string.
        """
        data = self._call().data
        encodings = ['utf-8', 'ISO-8859-1', 'Windows-1251', 'Windows-1252']

        for en in encodings:
            try:
                return data.decode(encoding=en)
            except (LookupError, UnicodeDecodeError):
                continue

        raise ValueError('Unable to decode data.')

    def call_to_response(self) -> HTTPResponse:
        """
        Calls a specified endpoint with specified parameters.

        :return: Http response.
        """
        return self._call()

    def _call(self) -> HTTPResponse:
        """
        Initiates a call to a specified endpoint with specified parameters.

        :return: Http response object.
        """
        return HttpCall.call(
            method=self.http_method,
            url=self.endpoint_url,
            fields=self.fields,
            headers=self.headers,
            body=self.http_body
        )

    @property
    def endpoint_url(self):
        """
        Url endpoint.

        :return: Url endpoint to call.
        """
        return self.__endpoint_url

    @property
    def http_method(self):
        """
        Endpoint request method type.

        :return: Request method type.
        """
        return self.__http_method

    @property
    def http_body(self) -> Optional[bytes]:
        """
        Endpoint request body represented as bytes.

        :return: Request body.
        """
        if isinstance(self.__http_body, (dict, list, tuple)):
            return json.dumps(self.__http_body).encode('UTF-8')

        if isinstance(self.__http_body, str):
            return self.__http_body.encode('UTF-8')

        if isinstance(self.__http_body, bytes):
            return self.__http_body

        return None

    @property
    def headers(self) -> Dict[str, str]:
        """
        All request headers associated with this endpoint.

        :return: Endpoint request headers.
        """
        headers = {}

        if isinstance(self.__http_body, (dict, list, tuple)):
            headers['Content-Type'] = 'application/json'
        elif isinstance(self.__http_body, str):
            headers['Content-Type'] = 'application/text'
        elif isinstance(self.__http_body, bytes):
            headers['Content-Type'] = 'application/octet-stream'

        return {
            **headers,
            **(self.__headers or {})
        }

    @property
    def fields(self) -> Optional[Any]:
        """
        An appropriate encoding of fields based on the HTTP method used when performing the request.
        An http request using urllib3.request.urlopen will be made using these fields.

        :return: Fields parameter.
        """
        return self.__fields
