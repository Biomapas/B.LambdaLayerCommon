from decimal import Decimal
from json import JSONEncoder
from typing import Any


class DecimalEncoder(JSONEncoder):
    """
    Custom JSONEncoder.

    This encoder checks whether the type of data is Decimal and converts it to float.
    Decimals are usually returned from DynamoDB table if the value is a number.
    """

    def default(self, o: Any):
        if isinstance(o, Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)
