from django.db import models

# Create your models here.
class Account(models.Model):
    accntType = models.CharField(max_length=10)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)
    password = models.IntegerField()
    accntInfo = models.JSONField()
