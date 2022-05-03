import json
import uuid
from typing import Any, Dict, Optional, Union
from json.decoder import JSONDecodeError

import boto3
from botocore.client import BaseClient
from botocore.config import Config


class SfnCall:
    CUSTOM_BOTO3_CONFIG = Config(
        # Give a maximum timeout which is equal to maximum lambda execution time.
        read_timeout=900
    )

    def __init__(self, state_machine_arn: str, client: BaseClient = None):
        service_name = 'stepfunctions'
        if client and client.meta.service_model.service_name != service_name:
            raise ValueError(f'Improper Boto3 client is provided. Only "{service_name}" client is accepted.')

        self.__sfn_client = client or boto3.client(service_name, config=self.CUSTOM_BOTO3_CONFIG)
        self.__state_machine_arn = state_machine_arn

    def call(self, data: Dict[Any, Any]) -> Union[str, Dict[str, Any]]:
        response = self.__sfn_client.start_sync_execution(
            stateMachineArn=self.__state_machine_arn,
            name=str(uuid.uuid4()),
            input=json.dumps(data)
        )

        response_status = response.get('status')
        response_error = response.get('error')

        if response_status != 'SUCCEEDED':
            raise ValueError(
                f'Failed to call step functions state machine: {response_error}. '
                f'Read logs for more info.'
            )

        output = json.loads(response.get('output', {}))
        # Add http-like handling that does not break anything.
        output = self.__http_like_handling(output)

        return output

    @staticmethod
    def __http_like_handling(output: Dict[Any, Any]) -> Union[str, Dict[str, Any]]:
        """
        A function that treats responses/outputs from step functions state machine as an http response:
        for example, it looks for keys like "http_status" or "body".

        :param output: The output data from step functions state machine.

        :return: Original output, if the output does not contain http-like features
            Body of the output otherwise (JSON deserialized, if possible).
        """
        http_status: Optional[int] = output.get('http_status') or output.get('statusCode')

        if isinstance(body := output.get('body'), str):
            try:
                http_body = json.loads(body)
            except (JSONDecodeError, TypeError):
                http_body = body
        else:
            http_body = body

        if isinstance(http_status, int):
            if http_status >= 400:
                try:
                    error_message = json.dumps(http_body)
                except (JSONDecodeError, TypeError):
                    error_message = http_body

                raise ValueError(error_message)

            return http_body

        return output
