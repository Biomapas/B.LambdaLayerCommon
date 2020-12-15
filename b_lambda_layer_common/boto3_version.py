from enum import Enum
from typing import Optional


class Boto3Version:
    class Boto3VersionType(Enum):
        NONE = 'NONE'
        SPECIFIC = 'SPECIFIC'
        LATEST = 'LATEST'

    def __init__(self, version: Optional[str] = None, version_type: Optional[Boto3VersionType] = None):
        self.__version = version
        self.__version_type = version_type

    @property
    def version_string(self) -> Optional[str]:
        return self.__version

    @property
    def version_type(self) -> Boto3VersionType:
        return self.__version_type

    @classmethod
    def from_string_version(cls, version_string: str) -> 'Boto3Version':
        return cls(version=version_string, version_type=cls.Boto3VersionType.SPECIFIC)

    @classmethod
    def latest(cls) -> 'Boto3Version':
        return cls(version_type=cls.Boto3VersionType.LATEST)

    @classmethod
    def dont_install(cls) -> 'Boto3Version':
        return cls(version_type=cls.Boto3VersionType.NONE)
