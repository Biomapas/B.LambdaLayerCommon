import json
from decimal import Decimal

from b_lambda_layer_common.util.decimal_encoder import DecimalEncoder


def test_FUNC_default_WITH_dictionary_with_decimals_EXPECT_successful_serialization() -> None:
    """
    Checks whether serialization works.

    :return: No return.
    """
    d = {
        'key': Decimal(1)
    }

    try:
        json.dumps(d)
    except TypeError:
        pass
    else:
        raise AssertionError('Expected to fail.')

    json.dumps(d, cls=DecimalEncoder)
