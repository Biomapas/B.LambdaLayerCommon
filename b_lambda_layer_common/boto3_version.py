from enum import Enum
from typing import Optional


class Boto3Version:
    class Boto3VersionType(Enum):
        NONE = 'NONE'
        SPECIFIC = 'SPECIFIC'
        LATEST = 'LATEST'

    def __init__(self):
        self.__version: Optional[str] = None
        self.__version_type: Optional[Boto3Version.Boto3VersionType] = None

    @property
    def version_string(self) -> str:
        return self.__version

    @property
    def version_type(self) -> Boto3VersionType:
        return self.__version_type

    @staticmethod
    def from_string_version(version_string: str) -> 'Boto3Version':
        version = Boto3Version()
        version.__version = version_string
        version.__version_type = Boto3Version.Boto3VersionType.SPECIFIC
        return version

    @staticmethod
    def latest() -> 'Boto3Version':
        version = Boto3Version()
        version.__version_type = Boto3Version.Boto3VersionType.LATEST
        return version

    @staticmethod
    def dont_install() -> 'Boto3Version':
        version = Boto3Version()
        version.__version_type = Boto3Version.Boto3VersionType.NONE
        return version
