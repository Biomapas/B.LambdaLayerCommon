import pytest

from b_lambda_layer_common.exceptions.container.internal_error import InternalError
from b_lambda_layer_common.exceptions.container.malformed_permission_error import MalformedPermissionError
from b_lambda_layer_common.validation.value_validator import ValueValidator


@pytest.mark.parametrize(
    "custom_exception,expected_exception",
    [
        (None, ValueError),
        (ValueError, ValueError),
        (Exception, Exception),
        (MalformedPermissionError, MalformedPermissionError),
        (InternalError, InternalError)
    ]
)
def test_FUNC_any_function_WITH_custom_exceptions_EXPECT_custom_exceptions_raised(custom_exception, expected_exception) -> None:
    """
    Check whether custom exceptions work.

    :return: No return.
    """
    with pytest.raises(expected_exception):
        ValueValidator(None, custom_exception=custom_exception).not_null()


@pytest.mark.parametrize(
    "value,exception",
    [
        (None, True),
        ('', False),
        (object(), False),
    ]
)
def test_FUNC_not_null_WITH_various_inputs_EXPECT_appropriate_response(value, exception) -> None:
    """
    Check whether the validation works.

    :return: No return.
    """
    exception_raised = False

    try:
        ValueValidator(value).not_null()
    except ValueError:
        exception_raised = True

    assert exception_raised == exception


@pytest.mark.parametrize(
    "value,exception",
    [
        (None, True),
        (1, True),
        (object(), True),
        ('', False),
        ('Hello world!', False)
    ]
)
def test_FUNC_is_str_WITH_various_inputs_EXPECT_appropriate_response(value, exception) -> None:
    """
    Check whether the validation works.

    :return: No return.
    """
    exception_raised = False

    try:
        ValueValidator(value).is_str()
    except ValueError:
        exception_raised = True

    assert exception_raised == exception


@pytest.mark.parametrize(
    "value,exception",
    [
        (None, True),
        (1, False),
        (object(), True),
        ('', True),
        ('Hello world!', True),
        (-1, False),
        (0.5, True)
    ]
)
def test_FUNC_is_int_WITH_various_inputs_EXPECT_appropriate_response(value, exception) -> None:
    """
    Check whether the validation works.

    :return: No return.
    """
    exception_raised = False

    try:
        ValueValidator(value).is_int()
    except ValueError:
        exception_raised = True

    assert exception_raised == exception


@pytest.mark.parametrize(
    "value,exception",
    [
        (None, True),
        (object(), True),
        ('', True),
        ([], True),
        ([1, 2, 3], False),
        ('Hello world!', False),
    ]
)
def test_FUNC_not_empty_WITH_various_inputs_EXPECT_appropriate_response(value, exception) -> None:
    """
    Check whether the validation works.

    :return: No return.
    """
    exception_raised = False

    try:
        ValueValidator(value).not_empty()
    except ValueError:
        exception_raised = True

    assert exception_raised == exception


@pytest.mark.parametrize(
    "value,exception",
    [
        (None, True),
        (object(), True),
        ([1, 2, 3], True),
        ([1, 2, 3, 4, 5], False),
        ('Hi', True),
        ('Hello world!', False),
    ]
)
def test_FUNC_min_len_WITH_various_inputs_EXPECT_appropriate_response(value, exception) -> None:
    """
    Check whether the validation works.

    :return: No return.
    """
    exception_raised = False

    try:
        ValueValidator(value).min_len(5)
    except ValueError:
        exception_raised = True

    assert exception_raised == exception


@pytest.mark.parametrize(
    "value,exception",
    [
        (None, True),
        (object(), True),
        ([1, 2, 3], False),
        ([1, 2, 3, 4, 5, 6], True),
        ('Hi', False),
        ('Hello world!', True),
    ]
)
def test_FUNC_max_len_WITH_various_inputs_EXPECT_appropriate_response(value, exception) -> None:
    """
    Check whether the validation works.

    :return: No return.
    """
    exception_raised = False

    try:
        ValueValidator(value).max_len(5)
    except ValueError:
        exception_raised = True

    assert exception_raised == exception


@pytest.mark.parametrize(
    "value,exception",
    [
        (None, True),
        (object(), True),
        ('LT', False),
        ('LTU', True),
    ]
)
def test_FUNC_is_country_iso2_WITH_various_inputs_EXPECT_appropriate_response(value, exception) -> None:
    """
    Check whether the validation works.

    :return: No return.
    """
    exception_raised = False

    try:
        ValueValidator(value).is_country_iso2()
    except ValueError:
        exception_raised = True

    assert exception_raised == exception


@pytest.mark.parametrize(
    "value,exception",
    [
        (None, True),
        (object(), True),
        ('LT', True),
        ('LTU', False),
    ]
)
def test_FUNC_is_country_iso3_WITH_various_inputs_EXPECT_appropriate_response(value, exception) -> None:
    """
    Check whether the validation works.

    :return: No return.
    """
    exception_raised = False

    try:
        ValueValidator(value).is_country_iso3()
    except ValueError:
        exception_raised = True

    assert exception_raised == exception


@pytest.mark.parametrize(
    "value,exception",
    [
        (None, True),
        (object(), True),
        ('2022.Aug.01', True),
        ('2022.08.01 1:2:3', True),
        ('2020-07-10', False),
        ('2020-07-10 15:00:00', False),
        ('2020-07-10 15:00:00.156', False)
    ]
)
def test_FUNC_is_str_date_WITH_various_inputs_EXPECT_appropriate_response(value, exception) -> None:
    """
    Check whether the validation works.

    :return: No return.
    """
    exception_raised = False

    try:
        ValueValidator(value).is_str_date()
    except ValueError:
        exception_raised = True

    assert exception_raised == exception


@pytest.mark.parametrize(
    "value,exception",
    [
        (None, True),
        (object(), True),
        ('hi@bob', True),
        ('hi.bob@bob.bob.bob', False),
        ('hello@world.com', False)
    ]
)
def test_FUNC_is_email_WITH_various_inputs_EXPECT_appropriate_response(value, exception) -> None:
    """
    Check whether the validation works.

    :return: No return.
    """
    exception_raised = False

    try:
        ValueValidator(value).is_email()
    except ValueError:
        exception_raised = True

    assert exception_raised == exception


@pytest.mark.parametrize(
    "value,exception",
    [
        (None, True),
        (object(), True),
        (1, True),
        (10, False),
    ]
)
def test_FUNC_min_number_WITH_various_inputs_EXPECT_appropriate_response(value, exception) -> None:
    """
    Check whether the validation works.

    :return: No return.
    """
    exception_raised = False

    try:
        ValueValidator(value).min_number(10)
    except ValueError:
        exception_raised = True

    assert exception_raised == exception


@pytest.mark.parametrize(
    "value,exception",
    [
        (None, True),
        (object(), True),
        (1, False),
        (11, True),
    ]
)
def test_FUNC_max_number_WITH_various_inputs_EXPECT_appropriate_response(value, exception) -> None:
    """
    Check whether the validation works.

    :return: No return.
    """
    exception_raised = False

    try:
        ValueValidator(value).max_number(10)
    except ValueError:
        exception_raised = True

    assert exception_raised == exception


@pytest.mark.parametrize(
    "value,exception",
    [
        (None, True),
        (object(), True),
        ('', True),
        ([], False),
        ([[], [], []], False)
    ]
)
def test_FUNC_is_list_WITH_various_inputs_EXPECT_appropriate_response(value, exception) -> None:
    """
    Check whether the validation works.

    :return: No return.
    """
    exception_raised = False

    try:
        ValueValidator(value).is_list()
    except ValueError:
        exception_raised = True

    assert exception_raised == exception


@pytest.mark.parametrize(
    "value,exception",
    [
        (None, True),
        (object(), True),
        ('', True),
        ([], False),
        ([[], [], []], True),
        (['hello', 'world', '!', ''], False)
    ]
)
def test_FUNC_is_list_of_strings_WITH_various_inputs_EXPECT_appropriate_response(value, exception) -> None:
    """
    Check whether the validation works.

    :return: No return.
    """
    exception_raised = False

    try:
        ValueValidator(value).is_list_of_strings()
    except ValueError:
        exception_raised = True

    assert exception_raised == exception


@pytest.mark.parametrize(
    "value,exception",
    [
        (None, True),
        (object(), True),
        ('', True),
        ('Bob', False),
        ('Bob123', False),
        ('!', True)
    ]
)
def test_FUNC_is_alphanumeric_WITH_various_inputs_EXPECT_appropriate_response(value, exception) -> None:
    """
    Check whether the validation works.

    :return: No return.
    """
    exception_raised = False

    try:
        ValueValidator(value).is_alphanumeric()
    except ValueError:
        exception_raised = True

    assert exception_raised == exception


@pytest.mark.parametrize(
    "value,exception",
    [
        (None, True),
        (object(), True),
        ('', True),
        ('Bob', False),
        ('Bob123', True),
        ('!', True),
        (' ', True)
    ]
)
def test_FUNC_alpha_only_WITH_various_inputs_EXPECT_appropriate_response(value, exception) -> None:
    """
    Check whether the validation works.

    :return: No return.
    """
    exception_raised = False

    try:
        ValueValidator(value).alpha_only()
    except ValueError:
        exception_raised = True

    assert exception_raised == exception


@pytest.mark.parametrize(
    "value,exception",
    [
        (None, True),
        (object(), True),
        ('', False),
        ('Bob', False),
        ([' '], False)
    ]
)
def test_FUNC_is_iterable_WITH_various_inputs_EXPECT_appropriate_response(value, exception) -> None:
    """
    Check whether the validation works.

    :return: No return.
    """
    exception_raised = False

    try:
        ValueValidator(value).is_iterable()
    except ValueError:
        exception_raised = True

    assert exception_raised == exception


@pytest.mark.parametrize(
    "value,exception",
    [
        (None, True),
        (object(), True),
        ('', True),
        ('BOB', True),
        ('Bob', False)
    ]
)
def test_FUNC_contains_lowercase_WITH_various_inputs_EXPECT_appropriate_response(value, exception) -> None:
    """
    Check whether the validation works.

    :return: No return.
    """
    exception_raised = False

    try:
        ValueValidator(value).contains_lowercase()
    except ValueError:
        exception_raised = True

    assert exception_raised == exception


@pytest.mark.parametrize(
    "value,exception",
    [
        (None, True),
        (object(), True),
        ('', True),
        ('Bob', False),
        ('bob', True)
    ]
)
def test_FUNC_contains_uppercase_WITH_various_inputs_EXPECT_appropriate_response(value, exception) -> None:
    """
    Check whether the validation works.

    :return: No return.
    """
    exception_raised = False

    try:
        ValueValidator(value).contains_uppercase()
    except ValueError:
        exception_raised = True

    assert exception_raised == exception


@pytest.mark.parametrize(
    "value,exception",
    [
        (None, True),
        (object(), True),
        (100, True),
        ('', True),
        ('bob', True),
        ('password1', False)
    ]
)
def test_FUNC_contains_digit_WITH_various_inputs_EXPECT_appropriate_response(value, exception) -> None:
    """
    Check whether the validation works.

    :return: No return.
    """
    exception_raised = False

    try:
        ValueValidator(value).contains_digit()
    except ValueError:
        exception_raised = True

    assert exception_raised == exception


@pytest.mark.parametrize(
    "value,exception",
    [
        (None, True),
        (object(), True),
        (100, True),
        ('', True),
        ('bob', True),
        ('password1', True),
        ('@password1!', False)
    ]
)
def test_FUNC_contains_special_WITH_various_inputs_EXPECT_appropriate_response(value, exception) -> None:
    """
    Check whether the validation works.

    :return: No return.
    """
    exception_raised = False

    try:
        ValueValidator(value).contains_special()
    except ValueError:
        exception_raised = True

    assert exception_raised == exception


@pytest.mark.parametrize(
    "value,exception",
    [
        ('', False),
        ('bob', False),
        ('bob ', True),
        (' ', True)
    ]
)
def test_FUNC_not_contains_whitespace_WITH_various_inputs_EXPECT_appropriate_response(value, exception) -> None:
    """
    Check whether the validation works.

    :return: No return.
    """
    exception_raised = False

    try:
        ValueValidator(value).not_contains_whitespace()
    except ValueError:
        exception_raised = True

    assert exception_raised == exception
