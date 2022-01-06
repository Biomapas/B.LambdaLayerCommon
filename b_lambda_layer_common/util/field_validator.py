import re

from datetime import datetime
from typing import Optional

from b_lambda_layer_common.exceptions.container.bad_request_error import BadRequestError


class FieldValidator:
    """
    Validates various values.
    """
    @staticmethod
    def max_length(string_field: Optional[str], max_length: int, allow_null_value: bool = True) -> None:
        """
        Checks whether the string is not too long.

        :param string_field: Field to check.
        :param max_length: Max length.
        :param allow_null_value: Allow string field to be null and not check max length.

        :return: No return.
        """
        if allow_null_value:
            if string_field is None:
                return

        if len(string_field) > max_length:
            raise BadRequestError(
                f'Field with value "{string_field}" is too long. '
                f'Max length is {max_length}.'
            )

    @staticmethod
    def country_iso_3(string_field: Optional[str], allow_null_value: bool = True):
        """
        Checks whether the string complies with ISO3.

        :param string_field: Field to check.
        :param allow_null_value: Allow string field to be null and not check the ISO3 standard.

        :return: No return.
        """
        if allow_null_value:
            if string_field is None:
                return

        if len(string_field) != 3:
            raise BadRequestError(f'Field with value "{string_field}" does not comply with ISO3 standard.')

    @staticmethod
    def string_date(string_field: Optional[str], allow_null_value: bool = True):
        """
        Checks whether the string complies with standard date format.

        :param string_field: Field to check.
        :param allow_null_value: Allow string field to be null and not check the date format.

        :return: No return.
        """
        if allow_null_value:
            if string_field is None:
                return
        try:
            datetime.fromisoformat(string_field)
        except ValueError as ex:
            raise BadRequestError(str(ex))

    @staticmethod
    def string_email(string_field: Optional[str], allow_null_value: bool = True):
        if allow_null_value:
            if string_field is None:
                return

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if not re.fullmatch(regex, string_field):
            raise BadRequestError(f'Field with value "{string_field}" is not an email.')
