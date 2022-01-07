from typing import Dict, Any

from b_lambda_layer_common.exceptions.container.unauthorized_error import UnauthorizedError


class CognitoAccessToken:
    """
    Class responsible for parsing Cognito Access Token parameters from API Gateway authorizer parameters.
    """

    def __init__(self, event: Dict[str, Any]) -> None:
        """
        Constructor.

        :param event: Lambda event.
        """
        try:
            self.__auth_token = event['headers']['authorization']

            # If JWT claims are not located in event.requestContext.authorizer.claims
            # they could be found in event.requestContext.authorizer instead.
            self.__claims = event['requestContext']['authorizer']['claims'] or event['requestContext']['authorizer']

            assert self.token_use == 'access'
        except (KeyError, AssertionError) as ex:
            raise UnauthorizedError('Missing access token.')

    @property
    def auth_token(self):
        return self.__auth_token

    @property
    def auth_time(self):
        return self.__claims['auth_time']

    @property
    def client_id(self):
        return self.__claims['client_id']

    @property
    def event_id(self):
        return self.__claims['event_id']

    @property
    def exp(self):
        return self.__claims['exp']

    @property
    def iat(self):
        return self.__claims['iat']

    @property
    def iss(self):
        return self.__claims['iss']

    @property
    def jti(self):
        return self.__claims['jti']

    @property
    def sub(self):
        return self.__claims['sub']

    @property
    def token_use(self):
        return self.__claims['token_use']

    @property
    def username(self) -> str:
        return self.__claims['username']
