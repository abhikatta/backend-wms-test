from django.db import models

# Create your models here.


class Item(models.Model):
    item_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name
