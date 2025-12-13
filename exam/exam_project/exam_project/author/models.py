from django.core.validators import MinLengthValidator
from django.db import models

from exam.exam_project.core import custom_validators


class Author(models.Model):
    MAX_LEN_FN = 40
    MIN_LEN_FN = 4

    MAX_LEN_LN = 50
    MIN_LEN_LN = 2

    MAX_LEN_PASS = 6

    first_name = models.CharField(
        max_length=MAX_LEN_FN,
        validators=(MinLengthValidator(MIN_LEN_FN), custom_validators.validate_all_letters),
        null=False,
        blank=False,
        verbose_name='First Name'
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LN,
        validators=(MinLengthValidator(MIN_LEN_LN), custom_validators.validate_all_letters),
        null=False,
        blank=False,
        verbose_name='Last Name'
    )

    passcode = models.CharField(
        max_length=MAX_LEN_PASS,
        validators=(custom_validators.validate_passcode,),
        null=False,
        blank=False,
    )
    pets_number = models.PositiveSmallIntegerField(
        null=False,
        blank=False,
        verbose_name='Pets Number',
    )

    info = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=True,
        blank=True,
        verbose_name='Profile Image URL',
    )





