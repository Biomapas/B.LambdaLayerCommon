from functools import wraps
from typing import Callable


def remove_header(*headers: str) -> Callable:
    """
    Decorator function removing given headers from event of API Gateway integration lambda.

    :param headers: Header names to remove.

    :return: Decorated function.
    """

    def wrapper(func: Callable):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            event = args[0]
            for header in headers:
                event.get('headers', {}).pop(header, None)
                event.get('multiValueHeaders', {}).pop(header, None)

            return func(*args, **kwargs)

        return wrapped_function

    return wrapper
