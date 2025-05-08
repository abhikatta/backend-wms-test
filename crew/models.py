from django.db import models

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

    def save(self, *args, **kwargs) -> None:
        # basically when is_active is updated by user, the others are also turned falsy, (common business logic)
        if not self.is_active:
            self.is_tasked = False
            self.hourly_wage = 0
            super().save(*args, **kwargs)

    def __str__(self):
        return self.name
