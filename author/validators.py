from django.core.exceptions import ValidationError


def validate_letters(value):
    if value.isalhpa is False:
        raise ValidationError('Your name must contain letters only!')


def validate_digits(value):
    if len(value) != 6 or not value.isdigit():
        raise ValidationError('Your name must contain letters only!')