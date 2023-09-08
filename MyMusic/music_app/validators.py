from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class NameContainsOnlyAlphaNumericAndUnderscore:
    def __call__(self, value):
        if not (value.isalnum() or '_' == value):
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")

    def __eq__(self, other):
        return True


@deconstructible
class PositiveFloatValidator:
    def __call__(self, value):
        if value < 0:
            raise ValidationError("Ensure this price is greater then or equal to 0.")

    def __eq__(self, other):
        return True
