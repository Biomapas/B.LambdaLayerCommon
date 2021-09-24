from enum import Enum
from typing import Optional


class PackageVersion:

    class VersionType(Enum):

        NONE = 'NONE'
        SPECIFIC = 'SPECIFIC'
        LATEST = 'LATEST'
        CUSTOM = 'CUSTOM'

    def __init__(self, version: Optional[str] = None, version_type: Optional[VersionType] = None):
        self.__version = version
        self.__version_type = version_type

    @property
    def version_string(self) -> Optional[str]:
        return self.__version

    @property
    def version_type(self) -> VersionType:
        return self.__version_type

    @classmethod
    def from_string_version(cls, version_string: str, custom: bool = False) -> 'PackageVersion':
        return cls(
            version=version_string,
            version_type=cls.VersionType.CUSTOM if custom else cls.VersionType.SPECIFIC
        )

    @classmethod
    def latest(cls) -> 'PackageVersion':
        return cls(version_type=cls.VersionType.LATEST)

    @classmethod
    def dont_install(cls) -> 'PackageVersion':
        return cls(version_type=cls.VersionType.NONE)
