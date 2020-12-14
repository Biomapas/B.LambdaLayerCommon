from aws_cdk.core import Stack, App

from b_lambda_layer_common.layer import Layer


def test_FUNC_constructor_WITH_various_parameters_EXPECT_layer_created():
    """
    Test whether the layer can be created.

    :return: No return.
    """
    layer = Layer(Stack(App(), 'Test'), 'Test')
    assert layer is not None
