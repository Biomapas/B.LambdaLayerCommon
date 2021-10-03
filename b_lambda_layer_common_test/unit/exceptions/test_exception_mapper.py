from b_lambda_layer_common.exceptions.container.already_exists_error import AlreadyExistsError
from b_lambda_layer_common.exceptions.exception_mapper import ExceptionMapper


def test_FUNC_map_and_raise_WITH_an_already_exists_identifier_EXPECT_appropriate_exception_thrown() -> None:
    """
    Test whether the function can map the exception correctly.

    :return: No return.
    """
    try:
        ExceptionMapper.map_and_raise('B_ALREADY_EXISTS')
    except AlreadyExistsError:
        pass
    else:
        raise AssertionError('Expected to fail.')
