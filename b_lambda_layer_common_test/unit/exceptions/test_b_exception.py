from b_lambda_layer_common.exceptions.b_exception import BException


def test_FUNC_message_WITH_no_message_EXPECT_default_message() -> None:
    """
    Test the default value for message.

    :return: No return.
    """
    class Test(BException):
        pass

    assert Test().message() == 'No message'


def test_FUNC_identifier_WITH_no_implementation_EXPECT_not_implemented_error() -> None:
    """
    Test whether the exception is thrown when the function is called.

    :return: No return.
    """
    try:
        BException.identifier()
    except NotImplementedError:
        pass
    else:
        raise AssertionError('Expected to fail.')


def test_FUNC_description_WITH_no_implementation_EXPECT_not_implemented_error() -> None:
    """
    Test whether the exception is thrown when the function is called.

    :return: No return.
    """
    try:
        BException.description()
    except NotImplementedError:
        pass
    else:
        raise AssertionError('Expected to fail.')


def test_FUNC_data_WITH_default_dummy_values_EXPECT_dictionary_created() -> None:
    """
    Test how the function creates a dictionary.

    :return: No return.
    """
    class Test(BException):
        @staticmethod
        def identifier() -> str:
            return 'DUMMY'

        @staticmethod
        def description() -> str:
            return 'Sample'

    assert Test().data() == {
        'message': 'No message',
        'identifier': 'DUMMY',
        'description': 'Sample'
    }
