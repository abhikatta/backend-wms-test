from django.db import models
from django.conf import settings


class Client(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone_number = models.BigIntegerField(unique=True)
    address = models.CharField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # the owner(basically the loggeed in user)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="clients",  # when reverse querying or something like that this is used like: user.clients.all()
        null=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
