from typing import Any, Dict, Optional

from b_lambda_layer_common.exceptions.container.forbidden_error import ForbiddenError


class ApiKey:
    def __init__(self, event: Dict[str, Any]):
        self.__event = event

    def get(self) -> str:
        return self.__extract()

    def __is_private_api(self) -> bool:
        return bool(self.__event.get('private_api', False))

    def __extract(self):
        if self.__is_private_api():
            api_key = self.__extract_private()
        else:
            api_key = self.__extract_public()

        if not api_key or not isinstance(api_key, str):
            raise ForbiddenError('Could not find api key string in the request.')

        return api_key

    def __extract_private(self) -> Optional[str]:
        api_key = self.__event.get('api_key')

        if not api_key or not isinstance(api_key, str):
            api_key = self.__event.get('ApiKey')

        return api_key

    def __extract_public(self) -> Optional[str]:
        api_key = self.__event.get('headers', {}).get('api_key')

        if not api_key or not isinstance(api_key, str):
            api_key = self.__event.get('headers', {}).get('ApiKey')

        if not api_key or not isinstance(api_key, str):
            api_key = self.__event.get('requestContext', {}).get('authorizer', {}).get('api_key')

        if not api_key or not isinstance(api_key, str):
            api_key = self.__event.get('requestContext', {}).get('authorizer', {}).get('ApiKey')

        return api_key
