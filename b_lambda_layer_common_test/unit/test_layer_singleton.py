import pytest
from aws_cdk.core import Stack, App

from b_lambda_layer_common.layer import Layer
from b_lambda_layer_common.layer_singleton import LayerSingleton


def test_ALL_FUNC_WITH_default_params_EXPECT_singleton_initialized():
    """
    Test whether the layer singleton works.

    :return: No return.
    """
    with pytest.raises(Exception):
        LayerSingleton(Stack(App(), 'Test'), 'Test')

    with pytest.raises(Exception):
        LayerSingleton.get_instance()

    assert LayerSingleton.is_initialized() is False

    LayerSingleton.initialize(Stack(App(), 'Test'), 'Test')

    with pytest.raises(Exception):
        LayerSingleton.initialize(Stack(App(), 'Test'), 'Test')

    LayerSingleton.safe_initialize(Stack(App(), 'Test'), 'Test')

    assert isinstance(LayerSingleton.get_instance().layer, Layer)
