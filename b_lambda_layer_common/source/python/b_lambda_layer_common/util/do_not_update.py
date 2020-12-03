class DoNotUpdate:
    """
    Helper to determine between provided and not provided 'None' parameters in request bodies.

    Usefull in such cases, where it has to be differentiated between a provided 'None' and a not provided parameter, when it is also by default 'None'.

    Examples
    ========

    >>> body = { 'param': None }
    >>> param = body.get('param', DoNotUpdate())
    >>> param
    None

    >>> body = {}
    >>> param = body.get('param', DoNotUpdate())
    >>> param
    <__main__.DoNotUpdate object at 0x7f321d0052e0>
    """
    pass
