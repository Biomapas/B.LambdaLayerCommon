from typing import Dict, Any


class Url:
    @staticmethod
    def from_event(event: Dict[Any, Any]) -> str:
        """
        Constructs a url of an api gateway resource that called this lambda function.

        :param event: Event passed to a lambda function upon invocation.

        :return: Parent API url.
        """
        try:
            return (
                f'{event["headers"]["X-Forwarded-Proto"]}://'
                f'{event["requestContext"]["domainName"]}/'
                f'{event["requestContext"]["stage"]}'
            )
        except KeyError as ex:
            raise ValueError(f'Can not construct API url from event. Missing keyword: {ex}.')
