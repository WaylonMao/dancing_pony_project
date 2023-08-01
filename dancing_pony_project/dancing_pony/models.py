from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=255, unique=True)


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(unique=True)
    image = models.ImageField(upload_to='dishes/')
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name
