import json
import uuid
from typing import Any, Dict, Optional

import boto3


class SfnCall:
    def __init__(self, state_machine_arn: str):
        self.__sfn_client = boto3.client('stepfunctions')
        self.__state_machine_arn = state_machine_arn

    def call(self, data: Dict[Any, Any]) -> Dict[Any, Any]:
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

        self.__output = json.loads(response.get('output', {}))
        # Add http-like handling that does not break anything.
        output = self.__http_like_handling()

        return output

    def __http_like_handling(self) -> Dict[str, Any]:
        """
        A function that treats responses/outputs from step functions state machine as an http response:
        for example, it looks for keys like "http_status" or "body".

        :param output: The output data from step functions state machine.

        :return: Original output, if the output does not contain http-like features
            Body of the output otherwise.
        """
        http_status: Optional[int] = self.__output.get('http_status') or self.__output.get('statusCode')
        http_body: Dict[str, Any] = self.__deserialize(self.__output)

        if isinstance(http_status, int):
            if http_status >= 400:
                raise ValueError(
                    f'Step functions state machine response indicated error (http status {http_status}). '
                    f'Response body: {http_body}.'
                )

            return http_body

        return self.__output

    @staticmethod
    def __deserialize(http_body: Dict[Any, Any]) -> Dict[str, Any]:
        if isinstance(body := http_body.get('body'), str):
            return json.loads(body)

        return http_body.get('body') or http_body
