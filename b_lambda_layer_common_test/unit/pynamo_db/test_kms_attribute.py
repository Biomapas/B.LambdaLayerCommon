from b_lambda_layer_common.pynamo_db.kms_attribute import KmsAttribute


def test_FUNC_serialize_WITH_null_value_EXPECT_serialzied() -> None:
    """
    Test whether the serialization works.

    :return: No return.
    """
    att = KmsAttribute(None, 'arn')
    att.serialize(None)


def test_FUNC_deserialize_WITH_null_value_EXPECT_deserialzied() -> None:
    """
    Test whether the serialization works.

    :return: No return.
    """
    att = KmsAttribute(None, 'arn')
    att.deserialize(None)
