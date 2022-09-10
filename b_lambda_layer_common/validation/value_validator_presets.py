from typing import Any, Optional, Type

from b_lambda_layer_common.validation.value_validator import ValueValidator


class ValueValidatorPresets(ValueValidator):
    def __init__(self, value: Any, custom_exception: Optional[Type[Exception]] = None):
        super().__init__(value, custom_exception)

    def is_username(self) -> 'ValueValidatorPresets':
        return (
            self.not_null()
                .is_str()
                .not_empty()
                .is_alphanumeric()
                .min_len(5)
                .max_len(100)
        )

    def is_password(self) -> 'ValueValidatorPresets':
        return (
            self.not_null()
                .is_str()
                .not_empty()
                .min_len(8)
                .max_len(100)
                .contains_digit()
                .contains_special()
                .contains_lowercase()
                .contains_uppercase()
        )

    def is_valid_str(self) -> 'ValueValidatorPresets':
        return (
            self.not_null()
                .is_str()
                .not_empty()
                .min_len(1)
                .max_len(100)
        )

    def is_name(self) -> 'ValueValidatorPresets':
        return (
            self.not_null()
                .is_str()
                .not_empty()
                .alpha_only()
                .min_len(1)
                .max_len(100)
        )

    def is_list_of_valid_strings(self) -> 'ValueValidatorPresets':
        self.is_list_of_strings()
        for item in self.value:
            ValueValidatorPresets(item).is_valid_str()
        return self
