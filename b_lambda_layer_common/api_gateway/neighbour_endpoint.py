from typing import Optional, Union, Dict, Any, Iterable, AnyStr

from b_lambda_layer_common.api_gateway.url import Url
from b_lambda_layer_common.util.http_endpoint import HttpEndpoint
from urllib3 import HTTPResponse


class NeighbourEndpoint:
    """
    Http caller class that is used to call other endpoints that belong to the same rest api.
    """

    def __init__(
            self,
            lambda_event: Dict[Any, Any],
            relative_endpoint: str,
            method: str,
            body: Optional[Union[Dict[Any, Any], Iterable[Any], AnyStr]] = None,
            headers: Optional[Dict[str, str]] = None,
            fields: Optional[Any] = None
    ) -> None:
        self.__lambda_event = lambda_event
        self.__relative_endpoint = relative_endpoint

        self.__http_endpoint = HttpEndpoint(
            endpoint_url=self.full_endpoint,
            method=method,
            body=body,
            headers=headers,
            fields=fields
        )

        if self.authorization_token:
            self.__http_endpoint.add_auth_token(self.authorization_token)

    def call(self) -> HTTPResponse:
        return self.__http_endpoint.call_to_response()

    @property
    def http_endpoint(self) -> HttpEndpoint:
        return self.__http_endpoint

    @property
    def parent_api(self) -> str:
        return Url.from_event(self.__lambda_event)

    @property
    def authorization_token(self) -> Optional[str]:
        return self.__lambda_event['headers'].get('authorization')

    @property
    def full_endpoint(self):
        parent_api = self.parent_api.rstrip('/\\').lstrip('/\\')
        relative_endpoint = self.__relative_endpoint.rstrip('/\\').lstrip('/\\')

        return f'{parent_api}/{relative_endpoint}'
