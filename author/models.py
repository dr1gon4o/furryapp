from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from .validators import validate_letters, validate_digits


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        blank=False,
        validators=[MinLengthValidator(4), validate_letters],
    )

    last_name = models.CharField(
        max_length=50,
        blank=False,
        validators=[MinLengthValidator(2), validate_letters],
    )

    passcode = models.CharField(
        max_length=6,
        blank=False,
        validators=[validate_digits],
        # Help_text="Your passcode must be a combination of 6 digits",
    )

    pets_number = models.PositiveIntegerField(
        blank=False,
        validators=[MinValueValidator(0)]
    )

    info = models.TextField(
            blank=True
    )

    image_url = models.URLField(
        blank=True
    )
