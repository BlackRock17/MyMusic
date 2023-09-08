from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def validate_string_alphanumeric(value):
    for ch in value:
        if not ch.isalnum() and ch != "_":
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


@deconstructible
class PositiveFloatValidator:
    def __call__(self, value):
        if value < 0:
            raise ValidationError("Ensure this price is greater then or equal to 0.")

    def __eq__(self, other):
        return True
