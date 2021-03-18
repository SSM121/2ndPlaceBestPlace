from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)
    password = models.IntegerField()
    acntInfo = JSONField()
