from typing import Any

from ordered_set import OrderedSet

from b_lambda_layer_common.util.decimal_encoder import DecimalEncoder


class DynamoDBEncoder(DecimalEncoder):
    def default(self, o: Any):
        if isinstance(o, (set, OrderedSet)):
            return list(o)
        return super(DynamoDBEncoder, self).default(o)
