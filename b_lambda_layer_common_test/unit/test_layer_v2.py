from aws_cdk.core import Stack, App
from b_lambda_layer_common.layer_v2 import LayerV2
from b_lambda_layer_common.package_version import PackageVersion


def test_FUNC_constructor_WITH_various_parameters_EXPECT_layer_created():
    """
    Test whether the layer can be created.

    :return: No return.
    """
    layer = LayerV2(Stack(App(), 'Test'), 'Test', {
        'jose': PackageVersion.latest()
    })

    assert layer is not None
