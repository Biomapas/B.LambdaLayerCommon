from typing import Any, Optional, Type

from b_lambda_layer_common.validation.value_validator import ValueValidator


class ValueValidatorPresets(ValueValidator):
    def __init__(self, value: Any, custom_exception: Optional[Type[Exception]] = None):
        super().__init__(value, custom_exception)

    def is_username(self, min_len: int = 1, max_len: int = 100) -> 'ValueValidatorPresets':
        return (
            self.not_null()
                .is_str()
                .not_empty()
                .not_contains_whitespace()
                .min_len(min_len)
                .max_len(max_len)
        )

    def is_password(self, min_len: int = 8) -> 'ValueValidatorPresets':
        return (
            self.not_null()
                .is_str()
                .not_empty()
                .min_len(min_len)
                .max_len(100)
                .contains_digit()
                .contains_special()
                .contains_lowercase()
                .contains_uppercase()
        )

    def is_valid_str(self, min_len: int = 1, max_len: int = 100) -> 'ValueValidatorPresets':
        return (
            self.not_null()
                .is_str()
                .not_empty()
                .min_len(min_len)
                .max_len(max_len)
        )

    def is_name(self, min_len: int = 1, max_len: int = 100) -> 'ValueValidatorPresets':
        return (
            self.not_null()
                .is_str()
                .not_empty()
                .min_len(min_len)
                .max_len(max_len)
        )

    def is_list_of_valid_strings(
            self,
            min_len: Optional[int] = None,
            max_len: Optional[int] = None,
            str_min_len: int = 1,
            str_max_len: int = 100
    ) -> 'ValueValidatorPresets':
        self.is_list_of_strings()
        if min_len: self.min_len(min_len)
        if max_len: self.max_len(max_len)
        for item in self.value:
            ValueValidatorPresets(item).is_valid_str(
                min_len=str_min_len,
                max_len=str_max_len
            )
        return self
