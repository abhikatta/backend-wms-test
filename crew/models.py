from django.db import models
from django.conf import settings
from clients.models import Client

ROLES = [
    ("carpenter", "Carpenter"),
    ("plumber", "Plumber"),
    ("electrician", "Electrician"),
    ("mason", "Mason"),
]


class Crew(models.Model):
    ROLE_CHOICES = ROLES
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_tasked = models.BooleanField(default=False)
    hourly_wage = models.IntegerField(default=0)
    role = models.CharField(choices=ROLE_CHOICES, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="crews",
        null=True,
    )
    client = models.ForeignKey(
        Client,  # or use the actual model path like 'yourapp.Client' if necessary
        on_delete=models.SET_NULL,  # SET_NULL allows retaining the crew member if the client is deleted
        null=True,
        blank=True,
        related_name="crew_members",
    )

    def save(self, *args, **kwargs) -> None:
        # basically when is_active is updated by user, the others are also turned falsy, (common business logic)

        if not self.is_active:
            self.is_tasked = False
            self.hourly_wage = 0

        # always keep an eye on the indentation and drop a line space
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
