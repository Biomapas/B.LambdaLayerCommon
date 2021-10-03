import logging
from typing import Optional, Any

from boto3 import client, Session

from b_lambda_layer_common.ssm.fetcher import Fetcher
from b_lambda_layer_common.ssm.refreshable import Refreshable

logger = logging.getLogger(__name__)


class SSMParameter(Refreshable):
    """
    SSM Parameter implementation.
    """

    def __init__(
            self,
            param_name: str,
            max_age: int = 0,
            ssm_client: Optional[client] = None
    ) -> None:
        """
        Constructor.

        :param param_name: SSM parameter name for which the value should be fetched.
        :param max_age: Max age of the value until refresh is needed.
        :param ssm_client: Boto3 SSM client (optional).
        """
        self.__ssm_client = ssm_client or Session().client('ssm')
        self.__ssm_fetcher = Fetcher(self.__ssm_client)

        super().__init__(max_age)

        self.__name = param_name
        self.__value: Any = None

    def update_value(self) -> None:
        """
        Force update of the SSM parameter value.

        :return: No return.
        """
        items, invalid_parameters = self.__ssm_fetcher.get_parameters([self.__name])

        if invalid_parameters or self.__name not in items:
            raise ValueError(f"{self.__name} is invalid.")

        self.__value = items[self.__name]['Value']

    @property
    def name(self) -> str:
        """
        Property for the SSM parameter name.

        :return: SSM parameter name.
        """
        return self.__name

    @property
    def value(self) -> Any:
        """
        Property for the SSM parameter value.

        :return: Value of the SSM parameter.
        """
        if self.__value is None:
            logger.info('Cached parameter value is none.')
            self.refresh()

        if self.should_refresh():
            logger.info('Cached parameter value should be refreshed.')
            self.refresh()

        return self.__value
