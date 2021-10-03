from typing import Any

from pynamodb.attributes import MapAttribute

from b_lambda_layer_common.util.dynamodb_encoder import DynamoDBEncoder


class PynamoDBEncoder(DynamoDBEncoder):
    def default(self, o: Any):
        if isinstance(o, MapAttribute):
            return o.as_dict()
        return super(PynamoDBEncoder, self).default(o)
