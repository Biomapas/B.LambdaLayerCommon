import functools
from typing import Any, Callable, Dict, Optional, Union


def skip_invocation(determinator: Optional[Union[str, bool, Callable[[Dict[str, Any], Any], bool]]] = None) -> Union[Callable, None]:
    """
    A decorator which allows to skip decorated function's execution if certain conditions are met.
    By default it returns decorated function's execution if no arguments are provided.
    If a determinator of type 'str' is provided, the decorator checks whether this key exists function's event 'dict' as parses result as 'bool' type.
    If a determinator of type 'bool' is provided, the decorator parses its value.
    If a callable object is provided as determinator, the decorator parses its value as 'bool'.
    Callable should accept 2 arguments - Lambda function's event and context.
    
    If any of the above evaluate to 'bool' of value True, the decorated function is not executed.

    :param determinator: An object which is used to evaluate whether to execute the decorated function.

    :return: Decorated function or None.


    Examples
    ========

    When no parameter is passed as decorator's determinator.

    >>> item = {'heartbeat': True}
    >>> context = ''
    >>> @skip_invocation()
    ... def handler(event, context):
    ...     return event
    >>> handler(item, context)
    {'heartbeat': True}

    When a 'bool' of value True is provided (decorated function does not invoke).

    >>> item = {'heartbeat': True}
    >>> context = ''
    >>> @skip_invocation(determinator=True)
    ... def handler(event, context):
    ...     return event
    >>> handler(item, context)
    >>>

    When a 'str' is provided which exists in event's 'dict' (decorated function does not invoke).

    >>> item = {'heartbeat': True}
    >>> context = ''
    >>> @skip_invocation(determinator="heartbeat")
    ... def handler(event, context):
    ...     return event
    >>> handler(item, context)
    >>>

    When a callable is provided which evaluates to True.
    Callable should take 2 arguments - Lambda function's event and context.

    >>> item = {'heartbeat': True}
    >>> context = ''
    >>> is_heartbeat = lambda e, c: "heartbeat" in e
    >>> @skip_invocation(determinator=is_heartbeat)
    ... def handler(event, context):
    ...     return event
    >>> handler(item, context)
    >>>

    """
    def wrapper(func):
        @functools.wraps(func)
        def wrapped_f(*args, **kwargs):
            skip = False
            event: Dict[str, Any] = args[0]
            context: Any = args[1]
            if isinstance(determinator, str):
                skip = bool(event.get(determinator, False))
            elif isinstance(determinator, bool):
                skip = determinator
            elif callable(determinator):
                skip = bool(determinator(event, context))
            
            if skip:
                return
            return func(*args, **kwargs)
        return wrapped_f
    return wrapper