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
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    ratings = models.JSONField(default=list)

    def __str__(self):
        return self.name

    def calculate_average_rating(self):
        if len(self.ratings) > 0:
            total_rating = sum(rating['rating'] for rating in self.ratings)
            return round(total_rating / len(self.ratings), 2)
        return 0.00
