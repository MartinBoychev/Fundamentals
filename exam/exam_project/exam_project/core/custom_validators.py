from django.core.exceptions import ValidationError


def validate_all_letters(name):
    if not name.isalpha():
        raise ValidationError('Your name must contain letters only!')


def validate_passcode(value):
    if not value.isdigit() or not len(value) == 6:
        raise ValidationError('Your passcode must be exactly 6 digits!')