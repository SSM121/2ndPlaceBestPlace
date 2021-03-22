from django.db import models
from django.urls import reverse  # used to generate URLs by reversing the URL patterns
import uuid  # required for Accounts to have a unique instance

class Account(models.Model):
    # Fields
    accntType = models.CharField(max_length=10, help_text='The type of Account: User, Owner, or Manager')
    name = models.CharField(max_length=40, help_text='Name of the user')
    email = models.EmailField(max_length=254, help_text='Email of the user')
    password = models.IntegerField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), help_text="Unique ID for this particular Account")
    accntInfo = models.JSONField()

    class Meta:
        ordering = ['email', 'accntType', 'name']

    def __str__(self):  # The __str__ method is useful  so if we want to print out an account we can.
        return self.name.__str__() + " owns an account type of: " + self.accntType.__str__() \
               + ". The email attatched to the account is " + self.email.__str__()

    def get_absolute_url(self):  # Not currently implemented Spencer Clemens working through a tutorial
        """ Returns the url to access a detailed recored of an account"""
        return reverse('account-detail', args=[str(self.email)])

