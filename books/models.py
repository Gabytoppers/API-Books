from django.db import models

# Create your models here.

class Book(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
            indexes = [
                models.Index(fields=['precio']),
            ]

    def __str__(self):
        return self.titulo