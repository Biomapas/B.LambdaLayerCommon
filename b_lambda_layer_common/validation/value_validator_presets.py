from typing import Any

from b_lambda_layer_common.validation.value_validator import ValueValidator


class ValueValidatorPresets:
    def __init__(self, value: Any):
        self.__value = value
        self.__validator = ValueValidator(value)

    def is_username(self) -> ValueValidator:
        return (
            self.__validator
                .not_null()
                .is_str()
                .not_empty()
                .is_alphanumeric()
                .min_len(5)
                .max_len(100)
        )

    def is_password(self) -> ValueValidator:
        return (
            self.__validator
                .not_null()
                .is_str()
                .not_empty()
                .min_len(8)
                .max_len(100)
                .contains_digit()
                .contains_special()
                .contains_lowercase()
                .contains_uppercase()
        )

    def is_valid_str(self) -> ValueValidator:
        return (
            self.__validator
                .not_null()
                .is_str()
                .not_empty()
                .min_len(1)
                .max_len(100)
        )

    def is_name(self) -> ValueValidator:
        return (
            self.__validator
                .not_null()
                .is_str()
                .not_empty()
                .alpha_only()
                .min_len(1)
                .max_len(100)
        )

    def is_list_of_valid_strings(self) -> ValueValidator:
        self.__validator.is_list_of_strings()
        for item in self.__value:
            ValueValidatorPresets(item).is_valid_str()
        return self.__validator
