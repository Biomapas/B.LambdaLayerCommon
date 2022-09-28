import pytest

from b_lambda_layer_common.validation.value_validator_presets import ValueValidatorPresets


@pytest.mark.parametrize(
    "value,exception",
    [
        (None, True),
        ('', True),
        (object(), True),
        ('bob1', False),
        ('bob 1', True),
        ('bob' * 50, True),
        ('HaX@R', False),
        ('Laimonas123', False),
    ]
)
def test_FUNC_is_username_WITH_various_inputs_EXPECT_appropriate_response(value, exception) -> None:
    """
    Check whether the validation works.

    :return: No return.
    """
    exception_raised = False

    try:
        ValueValidatorPresets(value).is_username()
    except ValueError:
        exception_raised = True

    assert exception_raised == exception


@pytest.mark.parametrize(
    "value,exception",
    [
        (None, True),
        ('', True),
        (object(), True),
        ('bob', True),
        ('bob' * 50, True),
        ('HaX@R', True),
        ('HX@R11111', True),
        ('Laimonas123', True),
        ('!abcABC123', False),
    ]
)
def test_FUNC_is_password_WITH_various_inputs_EXPECT_appropriate_response(value, exception) -> None:
    """
    Check whether the validation works.

    :return: No return.
    """
    exception_raised = False

    try:
        ValueValidatorPresets(value).is_password()
    except ValueError:
        exception_raised = True

    assert exception_raised == exception


@pytest.mark.parametrize(
    "value,exception",
    [
        (None, True),
        ('', True),
        (object(), True),
        ('bob', False),
    ]
)
def test_FUNC_is_valid_str_WITH_various_inputs_EXPECT_appropriate_response(value, exception) -> None:
    """
    Check whether the validation works.

    :return: No return.
    """
    exception_raised = False

    try:
        ValueValidatorPresets(value).is_valid_str()
    except ValueError:
        exception_raised = True

    assert exception_raised == exception


@pytest.mark.parametrize(
    "value,exception",
    [
        (None, True),
        ('', True),
        (object(), True),
        ('bob1', False),
        ('bob', False)
    ]
)
def test_FUNC_is_name_WITH_various_inputs_EXPECT_appropriate_response(value, exception) -> None:
    """
    Check whether the validation works.

    :return: No return.
    """
    exception_raised = False

    try:
        ValueValidatorPresets(value).is_name()
    except ValueError:
        exception_raised = True

    assert exception_raised == exception


@pytest.mark.parametrize(
    "value,exception",
    [
        (None, True),
        ('', True),
        (object(), True),
        ([], False),
        ([''], True),
        (['hi'], False),
        (['hi' * 100], True)
    ]
)
def test_FUNC_is_list_of_valid_strings_WITH_various_inputs_EXPECT_appropriate_response(value, exception) -> None:
    """
    Check whether the validation works.

    :return: No return.
    """
    exception_raised = False

    try:
        ValueValidatorPresets(value).is_list_of_valid_strings()
    except ValueError:
        exception_raised = True

    assert exception_raised == exception
