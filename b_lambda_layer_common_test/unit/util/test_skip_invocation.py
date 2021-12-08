from b_lambda_layer_common.util.skip_invocation import skip_invocation


def test_FUNC_with_default_skip_invocation_EXPECT_successful_return():
    """
    Check whether decorated function returns expected result when no parameters
    to decorator are passed.

    :return: No return.
    """
    item = {'heartbeat': True}

    @skip_invocation()
    def handler(event):
        return event

    response = handler(item)
    assert response is not None

def test_FUNC_with_bad_determinator_type_EXPECT_successful_return():
    """
    Check whether decorated function returns expected result when wrong
    determinator type is provided as parameter.

    :return: No return.
    """
    item = {'heartbeat': True}

    @skip_invocation(determinator={'test': 'test'})
    def handler(event):
        return event

    response = handler(item)
    assert response is not None

def test_FUNC_with_string_determinator_EXPECT_none_return():
    """
    Check whether decorated function is not invoked when determinator of type 'str'
    is provided and this key exists in event 'dict'.

    :return: No return.
    """
    item = {'heartbeat': True}

    @skip_invocation(determinator='heartbeat')
    def handler(event):
        return event

    response = handler(item)
    assert response is None

def test_FUNC_with_string_determinator_EXPECT_successful_return():
    """
    Check whether decorated function is invoked when determinator of type 'str'
    is provided and this key does not exist in event 'dict'.

    :return: No return.
    """
    item = {'heartbeat': True}

    @skip_invocation(determinator='test')
    def handler(event):
        return event

    response = handler(item)
    assert response is not None

def test_FUNC_with_bool_determinator_EXPECT_none_return():
    """
    Check whether decorated function is not invoked when a determinator of type 'bool'
    is provided and its value is True.

    :return: No return.
    """
    item = {'heartbeat': True}

    @skip_invocation(determinator=True)
    def handler(event):
        return event

    response = handler(item)
    assert response is None

def test_FUNC_with_bool_determinator_EXPECT_successful_return():
    """
    Check whether decorated function is invoked when a determinator of type 'bool'
    is provided and its value is False.

    :return: No return.
    """
    item = {'heartbeat': True}

    @skip_invocation(determinator=False)
    def handler(event):
        return event

    response = handler(item)
    assert response is not None

def test_FUNC_with_callable_determinator_EXPECT_none_return():
    """
    Check whether decorated function is not invoked when a 'callable' determinator is provided
    and it returns 'bool' of value True.

    :return: No return.
    """
    item = {'heartbeat': True}

    is_even = lambda x: x % 2 == 0

    @skip_invocation(determinator=is_even(4))
    def handler(event):
        return event

    response = handler(item)
    assert response is None

def test_FUNC_with_callable_determinator_EXPECT_successful_return():
    """
    Check whether decorated function is invoked when a 'callable' determinator is provided
    and it returns 'bool' of value False.

    :return: No return.
    """
    item = {'heartbeat': True}

    is_even = lambda x: x % 2 == 0

    @skip_invocation(determinator=is_even(5))
    def handler(event):
        return event

    response = handler(item)
    assert response is not None
