from typing import Optional, Any

from pynamodb.attributes import UnicodeAttribute


class KmsAttribute(UnicodeAttribute):
    def __init__(self, kms_boto_client: Any, kms_arn: str, *args, **kwargs):
        self.__kms_arn = kms_arn
        self.__kms_boto_client = kms_boto_client

        super().__init__(*args, **kwargs)

    def serialize(self, value: Optional[str] = None) -> Optional[str]:
        if value:
            encrypted = self.__encrypt(value).decode()
            return super().serialize(encrypted)

    def deserialize(self, value: Optional[str] = None) -> Optional[str]:
        if value:
            decrypted = self.__decrypt(value.encode())
            return super().deserialize(decrypted)

    def __encrypt(self, sensitive_data: str) -> bytes:
        return self.__kms_boto_client.encrypt(
            KeyId=self.__kms_arn,
            Plaintext=sensitive_data.encode()
        )['CiphertextBlob']

    def __decrypt(self, sensitive_data: bytes) -> str:
        return self.__kms_boto_client.decrypt(
            KeyId=self.__kms_arn,
            CiphertextBlob=sensitive_data
        )['Plaintext'].decode()
