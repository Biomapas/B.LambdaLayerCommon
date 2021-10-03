from typing import Any

from b_lambda_layer_common.util.decimal_encoder import DecimalEncoder


class DynamoDBEncoder(DecimalEncoder):
    def default(self, o: Any):
        if isinstance(o, set):
            return list(o)
        return super(DynamoDBEncoder, self).default(o)
