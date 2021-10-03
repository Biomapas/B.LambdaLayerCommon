from b_lambda_layer_common.exceptions.http_exception import HttpException


def test_FUNC_http_code_WITH_no_implementation_EXPECT_no_implemented_error_thrown() -> None:
    """
    Test whether the exception is thrown whether the function is called.

    :return: No return.
    """
    try:
        HttpException.http_code()
    except NotImplementedError:
        pass
    else:
        raise AssertionError('Expected to fail.')


def test_FUNC_data_WITH_dummy_values_EXPECT_dictionary_returned() -> None:
    """
    Test how the function creates corresponding dictionary.

    :return: No return.
    """
    class Test(HttpException):
        @staticmethod
        def identifier() -> str:
            return 'DUMMY'

        @staticmethod
        def description() -> str:
            return 'Sample'

        @staticmethod
        def http_code() -> int:
            return 500

    assert Test().data() == {
        'message': 'No message',
        'identifier': 'DUMMY',
        'description': 'Sample',
        'code': 500
    }
