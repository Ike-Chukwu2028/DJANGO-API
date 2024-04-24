from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField()
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)

