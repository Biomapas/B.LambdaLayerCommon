import logging
from abc import ABC, abstractmethod
from datetime import timedelta, datetime
from typing import Callable, List, Type, Optional
from functools import wraps

logger = logging.getLogger(__name__)


class Refreshable(ABC):
    """
    Abstract class for refreshable objects.
    """

    def __init__(self, max_age: int = 0) -> None:
        """
        Constructor.

        :param max_age: Max age in seconds of how long the refreshable object should live until expiration.
        """
        self.__max_age = max_age
        self.__max_age_delta = timedelta(seconds=max_age)
        self.__last_refresh_time = None

    @abstractmethod
    def update_value(self) -> None:
        """
        Abstract function that each refreshable type object should implement and
        define the logic of fetching and caching the value.

        :return: No return.
        """
        raise NotImplementedError()

    def refresh(self):
        """
        Initiate refresh action which forces to download a new value (update value)
        and updates the last refresh time for determining the next expiry.

        :return: No return.
        """
        logger.info('Refreshing value...')

        # Force update value.
        self.update_value()
        # Keep track of update date for determining the next expiry.
        self.update_refresh_time()

    def should_refresh(self) -> bool:
        """
        Tells whether the value should be (re)updated (refreshed).

        :return: True if should be updated, False otherwise.
        """
        # Never force refresh if no max_age is configured.
        if not self.__max_age:
            return False

        # Always force refresh if values were never fetched.
        if not self.__last_refresh_time:
            return True

        # Force refresh only if max_age seconds have expired.
        return datetime.utcnow() > self.__last_refresh_time + self.__max_age_delta

    def update_refresh_time(self) -> None:
        """
        Update internal refresh reference with current time.

        :return: No return.
        """
        now = datetime.utcnow()
        self.__last_refresh_time = now

    def refresh_on_error(
            self,
            error_classes: Optional[List[Type[Exception]]] = None,
            error_callback: Optional[Callable] = None,
    ) -> Callable:
        """
        Decorator to handle errors and retries.

        :param error_classes: Which errors to handle.
        :param error_callback: Which function to call in case specified errors are raised.

        :return: Decorator function.
        """
        if error_callback and not callable(error_callback):
            raise TypeError("Callback must be callable.")

        def decorator(func):
            """
            Actual func wrapper.
            """
            @wraps(func)
            def wrapped(*args, **kwargs):
                """
                Actual error/retry handling.
                """
                try:
                    return func(*args, **kwargs)
                except tuple(error_classes or [Exception]):
                    logger.exception('Got an error while calling the decorated function.')

                    self.refresh()

                    if error_callback:
                        logger.info(f'Calling callback function {str(error_callback)}...')
                        error_callback()
                    try:
                        logger.info('Calling the decorated function again...')
                        return func(*args, **kwargs)
                    except Exception:
                        logger.exception('After the value was refreshed we still ran into an error.')
                        raise
            return wrapped
        return decorator
