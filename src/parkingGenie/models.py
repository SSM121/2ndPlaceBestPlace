from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.urls import reverse  # used to generate URLs by reversing the URL patterns
import uuid  # required for Accounts to have a unique instance


class AccountManager(BaseUserManager):
    def _create_user(self, name, email, accountType, password=None, **extraFields):
        """
        Creates and saves a User with the given name, email and password
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            name=self.name,
            email=self.normalize_email(email),
            accountType=self.accountType,
            **extraFields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, name, email, accountType, password=None, **extraFields):
        return self._create_user(name, email, accountType, password, **extraFields)

    def create_superuser(self, name, email, accountType, password=None, **extraFields):
        """
        Creates and saves a superuser with the given name, email and password
        """
        user = self.create_user(
            name=name,
            email=email,
            password=password,
            accountType=accountType,
            **extraFields
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    # Fields
    USER_TYPE_CHOICES = (
        (1, 'customer'),
        (2, 'owner'),
        (3, 'manager'),
        (4, 'attendant'),
    )

    userType = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    name = models.CharField(max_length=40, help_text='Name of the user')
    email = models.EmailField(max_length=254, unique=True, help_text='Email of the user')
    password = models.CharField(max_length=15, help_text="The users password")
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4(), help_text="Unique ID for this particular Account")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'userType']

    objects = AccountManager()

    class Meta:
        ordering = ['email', 'name']

    def __str__(self):  # The __str__ method is useful  so if we want to print out an account we can.
        return self.name.__str__() + " owns an account type of: " + self.accountType.__str__() \
               + ". The email attached to the account is " + self.email.__str__()

    def get_absolute_url(self):
        """ Returns the url to access a detailed record of an account"""
        return "/users/%i/" % self.pk

    def get_email(self):
        return self.email


class Customer(models.Model):
    user = models.OneToOneField(Account, on_delete=CASCADE)
    carMake = models.CharField(max_length=15, help_text="Make of the customers car")
    carModel = models.CharField(max_length=15, help_text="Model of the customers car")
    carColor = models.CharField(max_length=15, help_text="Color of the customers car")
    carPlate = models.CharField(max_length=15, help_text="Licence plate of the customers car")

    class Meta:
        permissions = ['customer']


class Owner(models.Model):
    user = models.OneToOneField(Account, on_delete=CASCADE)
    parkingLots = models.JSONField(null=True, help_text="List of this owners parking lots")

    class Meta:
        permissions = ['owner']


class Manager(models.Model):
    user = models.OneToOneField(Account, on_delete=CASCADE)

    class Meta:
        permissions = ['manager']


class Attendant(models.Model):
    user = models.OneToOneField(Account, on_delete=CASCADE)
    # parkingLot = models.ForeignKey(ParkingLot, help_text="Parking Lot to which this attendant is assigned") # Need PL
    owner = models.ForeignKey(Owner, help_text="Owner of above parking lot")

    class Meta:
        permissions = ['attendant']
