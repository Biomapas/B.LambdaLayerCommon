import logging
from typing import Iterable, List, Tuple, Dict, Any, Union
from boto3 import client

logger = logging.getLogger(__name__)


class Fetcher:
    """
    Fetches parameters from SSM.
    """
    __MAX_PARAMS_SINGLE_FETCH = 10

    def __init__(self, ssm_client: client) -> None:
        """
        Constructor.

        :param ssm_client: Boto3 SSM client instance.
        """
        self.__ssm_client = ssm_client

    def get_parameters(self, names: List[str], with_decryption: bool = True) -> Tuple[Dict[str, Any], List[str]]:
        """
        Fetches parameters from SSM parameter store.

        :param names: Names of the SSM parameters.
        :param with_decryption: Should they be decrypted.

        :return: A tuple of objects:
            1. Dictionary of SSM parameters (items).
            2. List of invalid SSM parameter names.
        """
        items = {}
        invalid_names = []

        for name_batch in Fetcher.__batch(names, Fetcher.__MAX_PARAMS_SINGLE_FETCH):
            response = self.__ssm_client.get_parameters(
                Names=list(name_batch),
                WithDecryption=with_decryption,
            )

            invalid_names.extend(response['InvalidParameters'])

            for item in response['Parameters']:
                item['Value'] = self.__parse_value(item['Value'], item['Type'])
                items[item['Name']] = item

        logger.info(f'Fetched parameters: {items}.')

        return items, invalid_names

    @staticmethod
    def __parse_value(param_value, param_type) -> Union[str, List[str]]:
        """
        Parses value from SSM parameter.

        :param param_value: SSM parameter value.
        :param param_type: SSM parameter type.

        :return: Parsed value.
        """
        if param_type == 'StringList':
            return param_value.split(',')
        return param_value

    @staticmethod
    def __batch(iterable: Iterable, num: int) -> Iterable:
        """
        Turn an iterable into an iterable of batches of size n (or less, for the last one).

        :param iterable: Iterable to make chunks for.
        :param num: How many items per chunk.

        :return: Iterable of chunks.
        """
        length = len(list(iterable))
        for ndx in range(0, length, num):
            yield iterable[ndx:min(ndx + num, length)]
