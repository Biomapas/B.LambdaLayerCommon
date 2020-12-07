from abc import ABC, abstractmethod
from datetime import timedelta, datetime
from typing import Callable, List, Type, Optional
from functools import wraps


class Refreshable(ABC):
    """
    Abstract class for refreshable objects.
    """

    def __init__(self, max_age: int = 0):
        self.__last_refresh_time = None
        self.__max_age = max_age
        self.__max_age_delta = timedelta(seconds=max_age)

    @abstractmethod
    def re_fetch(self):
        raise NotImplementedError

    def refresh(self):
        """
        Updates the value(s) of this refreshable.
        """
        self.re_fetch()
        # Keep track of update date for max_age checks.
        self.__update_refresh_time()

    def refresh_on_error(
            self,
            error_classes: Optional[List[Type[Exception]]] = None,
            error_callback: Optional[Callable] = None,
    ) -> Callable:
        """
        Decorator to handle errors and retries.
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
                    self.refresh()

                    if error_callback:
                        error_callback()

                    return func(*args, **kwargs)
            return wrapped
        return decorator

    def __should_refresh(self):
        # Never force refresh if no max_age is configured.
        if not self.__max_age:
            return False

        # Always force refresh if values were never fetched.
        if not self.__last_refresh_time:
            return True

        # Force refresh only if max_age seconds have expired.
        return datetime.utcnow() > self.__last_refresh_time + self.__max_age_delta

    def __update_refresh_time(self, keep_oldest_value=False):
        """
        Update internal reference with current time.
        Optionally, keep the oldest available reference
        (used by groups with multiple fetch operations at potentially different times).
        """
        now = datetime.utcnow()

        if keep_oldest_value and self.__last_refresh_time:
            self.__last_refresh_time = min(now, self.__last_refresh_time)
        else:
            self.__last_refresh_time = now
