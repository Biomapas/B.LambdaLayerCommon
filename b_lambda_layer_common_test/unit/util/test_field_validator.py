import pytest

from b_lambda_layer_common.exceptions.container.bad_request_error import BadRequestError
from b_lambda_layer_common.util.field_validator import FieldValidator


def test_FUNC_max_length_WITH_too_long_string_EXPECT_exception_raised() -> None:
    """
    Check whether the validation succeeded.

    :return: No return.
    """
    with pytest.raises(BadRequestError):
        FieldValidator.max_length('RandomString', 5)


def test_FUNC_max_length_WITH_null_string_EXPECT_exception_not_raised() -> None:
    """
    Check whether the validation succeeded.

    :return: No return.
    """
    FieldValidator.max_length(None, 5)


def test_FUNC_max_length_WITH_good_string_EXPECT_exception_not_raised() -> None:
    """
    Check whether the validation succeeded.

    :return: No return.
    """
    FieldValidator.max_length('RandomString', 50, False)


def test_FUNC_country_iso_3_WITH_not_iso_string_EXPECT_exception_raised() -> None:
    """
    Check whether the validation succeeded.

    :return: No return.
    """
    with pytest.raises(BadRequestError):
        FieldValidator.country_iso_3('RandomString')


def test_FUNC_country_iso_3_WITH_null_string_EXPECT_exception_not_raised() -> None:
    """
    Check whether the validation succeeded.

    :return: No return.
    """
    FieldValidator.country_iso_3(None)


def test_FUNC_country_iso_3_WITH_good_string_EXPECT_exception_not_raised() -> None:
    """
    Check whether the validation succeeded.

    :return: No return.
    """
    FieldValidator.country_iso_3('LTU')


def test_FUNC_string_date_WITH_not_date_like_string_EXPECT_exception_raised() -> None:
    """
    Check whether the validation succeeded.

    :return: No return.
    """
    with pytest.raises(BadRequestError):
        FieldValidator.string_date('NotADate')


def test_FUNC_string_date_WITH_null_string_EXPECT_exception_not_raised() -> None:
    """
    Check whether the validation succeeded.

    :return: No return.
    """
    FieldValidator.string_date(None)


def test_FUNC_string_date_WITH_good_string_EXPECT_exception_not_raised() -> None:
    """
    Check whether the validation succeeded.

    :return: No return.
    """
    FieldValidator.string_date('2020-01-01')


def test_FUNC_string_email_WITH_non_email_string_EXPECT_exception_raised() -> None:
    """
    Check whether the validation succeeded.

    :return: No return.
    """
    with pytest.raises(BadRequestError):
        FieldValidator.string_email('dude.com')


def test_FUNC_string_email_WITH_null_string_EXPECT_exception_not_raised() -> None:
    """
    Check whether the validation succeeded.

    :return: No return.
    """
    FieldValidator.string_email(None)
    
    
def test_FUNC_string_email_WITH_good_string_EXPECT_exception_not_raised() -> None:
    """
    Check whether the validation succeeded.

    :return: No return.
    """
    FieldValidator.string_email('dude@email.com')
