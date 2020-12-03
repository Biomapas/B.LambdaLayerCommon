from typing import Iterable, List
from boto3 import client


class Fetcher:
    """
    Fetches parameters from SSM.
    """
    __MAX_PARAMS_SINGLE_FETCH = 10

    def __init__(self, ssm_client: client):
        self.__ssm_client = ssm_client

    def get_parameters(self, names: List[str], with_decryption: bool = False):
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

        return items, invalid_names

    @staticmethod
    def __parse_value(param_value, param_type):
        if param_type == 'StringList':
            return param_value.split(',')
        return param_value

    @staticmethod
    def __batch(iterable: Iterable, num: int):
        """
        Turn an iterable into an iterable of batches of size n (or less, for the last one).
        """
        length = len(list(iterable))
        for ndx in range(0, length, num):
            yield iterable[ndx:min(ndx + num, length)]
