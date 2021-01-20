import json
import logging
from typing import Dict, Any, Optional

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

try:
    from b_lambda_layer_common.exceptions.container.internal_error import InternalError
except ImportError as ex:
    logger.exception(f'Failed import.')
    from b_lambda_layer_common.source.python.b_lambda_layer_common.exceptions.container.internal_error import InternalError


class EventBridgeFactory:
    __client: Optional[Any] = None

    def __init__(
            self,
            source: str,
            detail_type: str,
            detail: Dict[Any, Any],
            event_bus_name: Optional[str] = None
    ) -> None:
        self.__source = source
        self.__detail_type = detail_type
        self.__detail = detail
        self.__event_bus_name = event_bus_name

    def emit(self, boto_client: Optional[Any] = None) -> None:
        if not boto_client and not self.__client:
            self.__client = boto3.client('events')

        boto_client = boto_client or self.__client

        event_entry = dict(
            Source=self.__source,
            DetailType=self.__detail_type,
            EventBusName=self.__event_bus_name,
            Detail=json.dumps(self.__detail),
        )

        try:
            response = boto_client.put_events(Entries=[event_entry])

            if response['FailedEntryCount'] != 0:
                errors = '\n'.join(entry.get('ErrorMessage') for entry in response['Entries'])
                raise InternalError(f'Failed to emit events: {errors}.')
        except ClientError as ex:
            raise InternalError(f'Failed to emit events ({str(ex)}).')
