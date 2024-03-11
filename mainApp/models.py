from django.db import models


class Kategoriya(models.Model):
    nom = models.CharField(max_length=255)
    rasm = models.ImageField(upload_to='kategoriyalar/', blank=True)

    def __str__(self):
        return self.nom


