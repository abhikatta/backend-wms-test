from django.db import models
from django.core.validators import validate_email


class User:
    email = models.EmailField(
        verbose_name="Email Address",
        unique=True,
        blank=False,
        max_length=254,
        validators=[validate_email],
    )
    first_name = models.CharField(
        verbose_name="First Name", max_length=254, blank=False
    )
    last_name = models.CharField(
        verbose_name="Last Name", max_length=254, blank=True, default=""
    )

    USERNAME_FIELD = "email"
