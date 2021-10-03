import json
from decimal import Decimal

from pynamodb.attributes import MapAttribute

from b_lambda_layer_common.util.pynamodb_encoder import PynamoDBEncoder


def test_FUNC_default_WITH_map_attribute_EXPECT_successful_serialization() -> None:
    """
    Checks whether serialization works.

    :return: No return.
    """
    d = MapAttribute(attributes={
        'key': Decimal(1),
        'key2': {1, 2, 3, 3, 3, 3}
    })

    try:
        json.dumps(d)
    except TypeError:
        pass
    else:
        raise AssertionError('Expected to fail.')

    json.dumps(d, cls=PynamoDBEncoder)
