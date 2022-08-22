import base64
import json
import urllib.parse
from json import JSONDecodeError
from typing import Dict, Any

from b_lambda_layer_common.exceptions.container.bad_request_error import BadRequestError


class Body:
    """
    Class dedicated to parsing API Gateway formed event bodies sent to Lambda functions.
    """

    def __init__(self, event: Dict[str, Any]):
        """
        Constructor.

        :param event: Lambda event.
        """
        self.__event = event
        self.__is_base_64_encoded = event.get('isBase64Encoded', False)

    def __is_private_api(self) -> bool:
        return bool(self.__event.get('private_api', False))

    def from_urlencoded(self) -> Dict[str, Any]:
        """
        Loads a urlencoded body as a dictionary.

        Example:
            in: TaskAttributes=%7B%22from_country%22%3A%22LT%22%7D&TaskPriority=0
            out: {'TaskAttributes': {'from_country': 'LT'}, 'TaskPriority': 0}

        :return: Event body as a dictionary.
        """
        str_body = urllib.parse.unquote(self.decoded())
        parsed_body = {}

        for item in str_body.split('&'):
            # Parameter maxsplit=1 is important here, because sometimes values can be other URLs containing '=' signs.
            # Example:
            #   in: 'UrlAttribute=https://www.example.com/example?param1=one&param2=two'
            #   out with maxsplit=1: ['UrlAttribute', 'https://www.example.com/example?param1=one&param2=two']
            key, value = item.split('=', maxsplit=1)
            try:
                parsed_body[key] = json.loads(value)
            except JSONDecodeError:
                parsed_body[key] = value

        return parsed_body

    def from_json(self) -> Dict[str, Any]:
        """
        Loads a JSON body as a dictionary.

        Example:
            in: "{\"email\":\"email@biomapas.com\",\"group_id\":\"abc1\"}"
            out: {'email': 'email@biomapas.com', 'group_id': 'abc1'}

        :return: Event body as a dictionary.
        """
        try:
            return json.loads(self.decoded())
        except JSONDecodeError as ex:
            raise BadRequestError(f'Malformed JSON body: {ex}.')

    def decoded(self) -> str:
        """
        Makes sure the body is not Base64 encoded.

        Example:
            in: SGVsbG8gd29ybGQh
            out: Hello world!


        :return: Event body in string format.
        """
        if self.__is_private_api():
            return json.dumps(self.__event)

        if self.__is_base_64_encoded:
            return base64.b64decode(self.__event['body']).decode()

        return self.__event['body']
