class _DoNotUpdateType:
    """
    Helper to determine between provided and not provided 'None' parameters in request bodies.

    Usefull in such cases, where it has to be differentiated between a provided 'None'
    and a parameter that wasn't provided, when it is also by default 'None'.

    Examples
    ========

    >>> body = { 'param': None }
    >>> param = body.get('param', DoNotUpdate())
    >>> param
    None

    >>> body = {}
    >>> param = body.get('param', DoNotUpdate())
    >>> param
    DoNotUpdate
    """
    _instance = None

    def __repr__(self):
        """
        Convenience method to pretty print the object name.
        """
        return "DoNotUpdate"

    def __new__(cls):
        """
        New instance creation.

        Prevents several objects of this class from existing. Normally this wouldn't be needed,
        but it's not much code to avoid the edge cases.
        """
        if cls._instance is None:
            cls._instance = super(_DoNotUpdateType, cls).__new__(cls)
        return cls._instance

    def __call__(self):
        """
        Hack to enable usage in annotations.
        """
        return self


DoNotUpdate = _DoNotUpdateType()
