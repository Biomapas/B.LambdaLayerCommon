import os


class OSParameter:
    def __init__(self, name: str):
        self.__name = name

    @property
    def value(self):
        """
        The value of a given param name in an operating system.
        """
        try:
            value = os.environ[self.__name]
        except KeyError:
            raise KeyError(f'Parameter with a name {self.__name} does not exist.')

        return value
