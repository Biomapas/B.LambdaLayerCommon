import os

from b_lambda_layer_common.util.os_parameter import OSParameter


def test_FUNC_value_WITH_existing_os_value_EXPECT_value_returned():
    """
    Test whether the value was retrieved from OS.

    :return: No return.
    """
    os.environ['TestValue-abc-123'] = 'ExampleValue'
    parameter = OSParameter('TestValue-abc-123')

    assert parameter.value == 'ExampleValue'
