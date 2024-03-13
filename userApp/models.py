from django.db import models
from django.contrib.auth.models import AbstractUser


class Profil(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    confirmation_code = models.CharField(max_length=6, blank=True, null=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
