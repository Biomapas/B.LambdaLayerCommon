from typing import Optional

from b_lambda_layer_common.util.os_parameter import OSParameter
from boto3 import client
from pynamodb.attributes import UnicodeAttribute

KMS_CLIENT = client('kms')
KMS_CMK_ARN = OSParameter('KMS_CMK_ARN')


class KmsAttribute(UnicodeAttribute):
    def serialize(self, value: Optional[str] = None) -> Optional[str]:
        if value:
            encrypted = self.__encrypt(value).decode()
            return super().serialize(encrypted)

    def deserialize(self, value: Optional[str] = None) -> Optional[str]:
        if value:
            decrypted = self.__decrypt(value.encode())
            return super().deserialize(decrypted)

    @staticmethod
    def __encrypt(sensitive_data: str) -> bytes:
        return KMS_CLIENT.encrypt(
            KeyId=KMS_CMK_ARN.value,
            Plaintext=sensitive_data.encode()
        )['CiphertextBlob']

    @staticmethod
    def __decrypt(sensitive_data: bytes) -> str:
        return KMS_CLIENT.decrypt(
            KeyId=KMS_CMK_ARN.value,
            CiphertextBlob=sensitive_data
        )['Plaintext'].decode()
