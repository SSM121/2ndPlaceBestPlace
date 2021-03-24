from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.urls import reverse  # used to generate URLs by reversing the URL patterns
import uuid  # required for Accounts to have a unique instance


class AccountManager(BaseUserManager):
    def create_user(self, name, email, password=None):
        """
        Creates and saves a User with the given name, email and password
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            name=self.name,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password=None):
        """
        Creates and saves a superuser with the given name, email and password
        """
        user = self.create_user(
            name=name,
            email=email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    # Fields
    # accountType = models.CharField(max_length=10, help_text='The type of Account: User, Owner, or Manager')
    name = models.CharField(max_length=40, help_text='Name of the user')
    email = models.EmailField(max_length=254, unique=True, help_text='Email of the user')
    password = models.CharField(max_length=15, help_text="The users password")
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4(), help_text="Unique ID for this particular Account")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = 'name'

    class Meta:
        ordering = ['email', 'name']

    def __str__(self):  # The __str__ method is useful  so if we want to print out an account we can.
        return self.name.__str__() + " owns an account type of: " + self.accntType.__str__() \
               + ". The email attatched to the account is " + self.email.__str__()

    def get_absolute_url(self):  # Not currently implemented Spencer Clemens working through a tutorial
        """ Returns the url to access a detailed recored of an account"""
        return reverse('account-detail', args=[str(self.email)])


class Customer(Account):
    carMake = models.CharField(max_length=15, help_text="Make of the customers car")
    carModel = models.CharField(max_length=15, help_text="Model of the customers car")
    carColor = models.CharField(max_length=15, help_text="Color of the customers car")
    carPlate = models.CharField(max_length=15, help_text="Licence plate of the customers car")

    class Meta:
        permissions = ['customer']


class Owner(Account):
    parkingLots = models.JSONField(null=True, help_text="List of this owners parking lots")

    class Meta:
        permissions = ['owner']


class Manager(Account):
    class Meta:
        permissions = ['manager']


class Attendant(Account):
    # parkingLot = models.ForeignKey(ParkingLot, help_text="Parking Lot to which this attendant is assigned") # Need PL
    owner = models.ForeignKey(Owner, help_text="Owner of above parking lot")

    class Meta:
        permissions = ['attendant']
