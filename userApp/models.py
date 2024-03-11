from django.db import models
from django.contrib.auth.models import AbstractUser


class Profil(AbstractUser):
    tel = models.CharField(max_length=20, blank=True, null=True)
    jins = models.CharField(max_length=20, blank=True, null=True)
    t_sana = models.DateField(blank=True, null=True)
    davlat = models.CharField(max_length=255, blank=True, null=True)
    shahar = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username
