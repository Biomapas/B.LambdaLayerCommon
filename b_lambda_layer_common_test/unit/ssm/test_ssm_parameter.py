from b_lambda_layer_common.ssm.ssm_parameter import SSMParameter
from .dummy_ssm_client import DummySsmClient


def test_FUNC_refresh_AND_value_WITH_multiple_calls_EXPECT_values_refreshed():
    """
    Test whether the parameter can fetch and refreshed from SSM.

    :return: No return.
    """
    dummy_client = DummySsmClient()

    # Assert #1: No calls to get_parameters were done.
    assert dummy_client.get_parameters_function_calls == 0

    parameter = SSMParameter(
        param_name='TestParameter',
        ssm_client=dummy_client
    )

    # Assert #2: Still no calls to get_parameters.
    assert dummy_client.get_parameters_function_calls == 0

    value1 = parameter.value

    # Assert #3: One call to get_parameters.
    assert dummy_client.get_parameters_function_calls == 1

    value2 = parameter.value

    # Assert #3: Still one call to get_parameters, because value is now cached.
    assert dummy_client.get_parameters_function_calls == 1
    # Assert #4: Both values are the same.
    assert value1 == value2

    parameter.refresh()

    # Assert #5: Second call to get_parameters, because refresh was called.
    assert dummy_client.get_parameters_function_calls == 2

    value3 = parameter.value

    # Assert #6: Still two calls to get_parameters, because value is cached.
    assert dummy_client.get_parameters_function_calls == 2
    # Assert #7: The new refreshed value is different.
    assert (value1 == value2) and (value2 != value3)


def test_FUNC_refresh_on_error_WITH_multiple_decorators_EXPECT_values_refreshed():
    """
    Test whether the decorators work.

    :return: No return.
    """
    dummy_client = DummySsmClient()

    parameter = SSMParameter(
        param_name='TestParameter',
        ssm_client=dummy_client
    )

    outer_decorator_callbacks = 0
    inner_decorator_callbacks = 0

    def callback_function_outer():
        nonlocal outer_decorator_callbacks
        outer_decorator_callbacks += 1

    def callback_function_inner():
        nonlocal inner_decorator_callbacks
        inner_decorator_callbacks += 1

    # Should result in 1st refresh.
    @parameter.refresh_on_error(error_callback=callback_function_outer)
    # Should result in 2nd refresh.
    @parameter.refresh_on_error(error_callback=callback_function_inner)
    def decorated_function():
        nonlocal inner_decorator_callbacks
        nonlocal outer_decorator_callbacks

        # Should result in 3rd refresh.
        print(parameter.value)

        if inner_decorator_callbacks == 0 or outer_decorator_callbacks == 0:
            raise Exception('Lets raise some exceptions!')

    decorated_function()

    assert outer_decorator_callbacks == 1
    assert inner_decorator_callbacks == 1
    assert dummy_client.get_parameters_function_calls == 3
