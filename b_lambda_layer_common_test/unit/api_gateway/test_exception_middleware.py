from b_lambda_layer_common.api_gateway.exception_middleware import exception_middleware
from b_lambda_layer_common.exceptions.container.dependency_error import DependencyError


def test_FUNC_exception_middleware_WITH_function_raises_dependency_error_EXPECT_dependency_error_code_424() -> None:
    """
    Test that exception middleware can actually catch exceptions and return serialized ones.

    :return: No return.
    """

    @exception_middleware
    def dummy_function():
        raise DependencyError()

    data = dummy_function()

    assert data['statusCode'] == 424
