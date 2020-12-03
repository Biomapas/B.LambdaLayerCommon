import logging
from typing import Optional, Tuple
from boto3 import client, Session

logger = logging.getLogger(__name__)

try:
    from b_lambda_layer_common.ssm.fetcher import Fetcher
    from b_lambda_layer_common.ssm.refreshable import Refreshable
except ImportError:
    logger.exception(f'Failed import.')
    from b_lambda_layer_common.source.python.b_lambda_layer_common.ssm.fetcher import Fetcher
    from b_lambda_layer_common.source.python.b_lambda_layer_common.ssm.refreshable import Refreshable


class SSMParameter(Refreshable):
    """
    SSM Parameter wrapper.
    """

    def __init__(
            self,
            param_name: str,
            max_age: int = 0,
            with_decryption: bool = True,
            ssm_client: Optional[client] = None
    ) -> None:
        ssm_client = ssm_client or Session().client('ssm')

        super().__init__(max_age)

        name, version, is_pinned = self.__parse_version(param_name)

        self.__name = name
        self.__version = version
        self.__is_pinned_version = is_pinned
        self.__with_decryption = with_decryption

        self.__fetcher = Fetcher(ssm_client)

        self.__value = None

    def re_fetch(self):
        """
        Force refresh of the configured param names.
        """
        items, invalid_parameters = self.__fetcher.get_parameters([self.full_name], self.__with_decryption)

        if invalid_parameters or self.__name not in items:
            raise ValueError(f"{self.__name} is invalid.")

        self.__value = items[self.__name]['Value']
        self.__version = items[self.__name]['Version']

    @property
    def name(self):
        """
        Name property.
        """
        return self.__name

    @property
    def full_name(self):
        """
        Name + version property.
        """
        if self.__version and self.__is_pinned_version:
            return f'{self.__name}:{self.__version}'

        return self.__name

    @property
    def version(self):
        """
        Version property.
        """
        if self.__version is None or self.__should_refresh():
            self.refresh()

        return self.__version

    @property
    def value(self):
        """
        The value of a given param name.
        """
        if self.__value is None or self.__should_refresh():
            self.refresh()

        return self.__value

    @staticmethod
    def __parse_version(param_name: str) -> Tuple[str, Optional[int], bool]:
        """
        Extracts version from full name, if provided.
        """
        name, version, is_pinned_version = param_name, None, False

        if ":" in param_name:
            name, version = param_name.split(':')

            if version.isdigit() and int(version) > 0:
                version = int(version)
                is_pinned_version = True
            else:
                raise ValueError(f"Invalid version: {version}.")

        return name, version, is_pinned_version
