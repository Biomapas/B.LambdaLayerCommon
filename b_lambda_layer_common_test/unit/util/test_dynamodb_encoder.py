import json
from decimal import Decimal

from ordered_set import OrderedSet

from b_lambda_layer_common.util.dynamodb_encoder import DynamoDBEncoder


def test_FUNC_default_WITH_decimals_and_sets_and_ordered_set_EXPECT_successful_serialization() -> None:
    """
    Checks whether serialization works.

    :return: No return.
    """
    d = {
        'key': Decimal(1),
        'key2': {1, 2, 3, 3, 3, 3},
        'key3': OrderedSet([1, 1, 2, 3, 2])
    }

    try:
        json.dumps(d)
    except TypeError:
        pass
    else:
        raise AssertionError('Expected to fail.')

    json.dumps(d, cls=DynamoDBEncoder)
