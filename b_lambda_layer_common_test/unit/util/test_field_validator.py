from b_lambda_layer_common.util.field_validator import FieldValidator


def test_CLASS_field_validator_WITH_nothing_EXPECT_class_initiated() -> None:
    """
    Check whether the class can be initiated. This is legacy backwards-compatible classs.

    :return: No return.
    """
    FieldValidator()
