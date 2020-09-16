from typing import Any
import logging

logger = logging.getLogger(__name__)

try:
    from b_lambda_layer_common.util.decimal_encoder import DecimalEncoder
except ImportError as ex:
    logger.exception(f'Failed import.')
    from b_lambda_layer_common.source.python.b_lambda_layer_common.util.decimal_encoder import DecimalEncoder


class DynamoDBEncoder(DecimalEncoder):
    def default(self, o: Any):
        if isinstance(o, set):
            return list(o)
        return super(DynamoDBEncoder, self).default(o)
