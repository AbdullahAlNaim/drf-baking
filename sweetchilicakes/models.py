from django.db import models

# Create your models here.
class Cakes(models.Model):
    cake_name = models.CharField(max_length=100)
    layers = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)