import logging
from typing import Any, Callable, Set, Union

logger = logging.getLogger(__name__)

# TODO: "Refreshable" class should be moved to a more appropriate location.
try:
    from b_lambda_layer_common.exceptions.container.internal_error import InternalError
    from b_lambda_layer_common.ssm.refreshable import Refreshable
except ImportError:
    logger.exception(f'Failed import.')
    from b_lambda_layer_common.source.python.b_lambda_layer_common.exceptions.container.internal_error import InternalError
    from b_lambda_layer_common.source.python.b_lambda_layer_common.ssm.refreshable import Refreshable


class InMemoryDataCache(Refreshable):
    """
    In-memory data cache implementation.
    """

    def __init__(self, max_age: int = 0):
        """
        Constructor.

        :param max_age: Max age of the cache until reset is needed.
        """
        super().__init__(max_age)

        self.__cache = {}

    def update_value(self) -> None:
        """
        Force reset of the cache.

        :return: No return.
        """
        self.__cache = {}

    def use_cache(self, pointer: Union[str, Set[str]], func: Callable, *args, **kwargs) -> Any:
        """
        Caches function return values.

        :param pointer: A string or a set of strings used to reference cached data.
        :param func: A function whose return value will be cached.
        :param args: Arguments that will be passed to func.

        :key kwargs: Keyword arguments that will be passed to func.

        :return: Cached data.
        """
        if self.should_refresh():
            logger.info('Cached data should be reset.')
            self.refresh()

        if not isinstance(pointer, (str, set)):
            raise InternalError('Type of pointer value must be str or set.')

        return self.__get_data(pointer) or self.__add_data(pointer, func, *args, **kwargs)

    def __get_data(self, pointer: Union[str, Set[str]]) -> Any:
        """
        Retrieves data from cache if possible.

        :param pointer: A string or a set of strings used to reference cached data.

        :return: Data if it's cached, otherwise None.
        """
        if isinstance(pointer, str) and pointer in self.__cache:
            data = self.__cache[pointer]
        elif isinstance(pointer, set) and pointer.issubset(self.__cache):
            data = {key: self.__cache[key] for key in pointer}
        else:
            data = None

        logger.info('Using cached data.' if data else 'Data not in cache.')

        return data

    def __add_data(self, pointer: Union[str, Set[str]], func: Callable, *args, **kwargs) -> Any:
        """
        Adds data to cache.

        :param pointer: A string or a set of strings used to reference cached data.
        :param func: A function whose return value will be cached.
        :param args: Arguments that will be passed to func.

        :key kwargs: Keyword arguments that will be passed to func.

        :return: Cached data.
        """
        logger.info('Adding data to cache...')

        data = func(*args, **kwargs)

        self.__cache.update(
            {pointer: data} if isinstance(pointer, str) else {key: data[key] for key in pointer}
        )

        return data
