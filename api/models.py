from django.db import models

# Create your models here.

class PriceData(models.Model):
    price = models.CharField(max_length=100)
