from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)
from django.urls import reverse  # used to generate URLs by reversing the URL patterns
from django.utils import timezone
import uuid  # required for Accounts to have a unique instance
from django.utils import timezone


class AccountManager(BaseUserManager):
    def create_user(self, name, email, userType, password=None, last_login=None, **extraFields):
        """
        Creates and saves a User with the given name, email and password
        """
        # User type isn't saved any where
        if not email:
            raise ValueError('Users must have an email address')

        now = timezone.now()
        user = self.model(
            userType=userType,
            name=name,
            email=self.normalize_email(email),
            last_login=now,
            **extraFields
        )

        user.set_password(password)
        user.save(using=self._db)  # Adds user to data base
        return user

    def create_superuser(self, name, email, password=None, **extraFields):
        """
        Creates and saves a superuser with the given name, email and password
        """

        now = timezone.now()
        user = self.create_user(
            name=name,
            email=email,
            password=password,
            last_login=now,
            **extraFields
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    # Fields
    USER_TYPE_CHOICES = (
        (1, 'Customer'),
        (2, 'Owner'),
        (3, 'Manager'),
        (4, 'Attendant'),
    )

    def __init__(self, name, email):
        self.name = models.CharField(max_length=40, help_text='Name of the user')
        self.email = models.EmailField(max_length=254, unique=True, help_text='Email of the user')
        self.userType = models.PositiveSmallIntegerField(default=1)
        self.password = models.CharField(max_length=15, help_text="The users password")
        self.last_login = models.DateTimeField(null=True, blank=True)
        self.is_superuser = models.BooleanField(default=True)  # Can turn back to false
        self.is_active = models.BooleanField(default=True)
        self.is_staff = models.BooleanField(default=True)  # Can turn back to false

        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = ['name', 'userType']  # password and email are automiatically required

        objects = AccountManager()
        objects.create_user(self.name, self.email, self.userType, self.password)  # User type passed as an int

    class Meta:
        ordering = ['email', 'name']

    def __str__(self):  # The __str__ method is useful  so if we want to print out an account we can.
        return self.name.__str__() + " owns an account type of: " + self.USER_TYPE_CHOICES.__str__() \
               + ". The email attached to the account is " + self.email.__str__()

    def get_absolute_url(self):
        """ Returns the url to access a detailed record of an account"""
        return "/users/%i/" % self.pk

    def get_email(self):
        return self.email


class Customer(models.Model):
     user = models.OneToOneField(Account, on_delete=models.CASCADE)
     carMake = models.CharField(max_length=15, help_text="Make of the customers car")
     carModel = models.CharField(max_length=15, help_text="Model of the customers car")
     carColor = models.CharField(max_length=15, help_text="Color of the customers car")
     carPlate = models.CharField(max_length=15, help_text="Licence plate of the customers car")


class Owner(models.Model):
     user = models.OneToOneField(Account, on_delete=models.CASCADE)
     parkingLots = models.JSONField(null=True, help_text="List of this owners parking lots")


class Manager(models.Model):
     user = models.OneToOneField(Account, on_delete=models.CASCADE)


class Event(models.Model):
     name = models.CharField(max_length=50, help_text="The long name of the event, with spaces")
     shortName = models.CharField(max_length=15, help_text="Short event name, used when creating attendant 'email' addresses")
     date = models.DateTimeField("Date", default=timezone.now)
     manager = models.ForeignKey(Manager, help_text="Manager who created the Event", on_delete=models.CASCADE)
     address = models.CharField(max_length=100, help_text="Address of the Event")

     def __str__(self):
         return "%s \n %s" % (self.name, self.address)

     def getShortName(self):
         return self.shortName

     def getAddress(self):
         return self.address


class ParkingLot(models.Model):
    # Fields
    name = models.CharField(max_length=20, help_text="The name of the parking lot")
    address = models.CharField(max_length=100, help_text="Address of the parking lot")
    parking = models.IntegerField(help_text="Number of available normal parking spaces")
    tailgate = models.IntegerField(help_text="Number of available tailgate parking spaces")
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, help_text="Owner of the parking lot")
    event = models.ManyToManyField(Event, help_text="Event(s) that will use this parking lot")
    date = models.DateField(help_text="Date of the Event")
    #distance = getDistance()
    price = models.DecimalField(max_digits=5, decimal_places=2, help_text="Cost of a normal parking spot", default=20.00)
    tailgatePrice = models.DecimalField(max_digits=5, decimal_places=2, help_text="Cost of a tailgate parking spot", default=30.00)

    class Meta:
        ordering = ['date', 'price', 'tailgatePrice']

    def __str__(self):  # Useful for printing out Name and Address of the parking lot
         return "%s \n %s" % (self.name, self.address)
         # return [self.name, self.address]  # If we find this works better for our purposes.

    def availSpots(self):   # Get the number of available normal parking spots
         return self.parking

    def availTailgate(self):    # Get the number of available tailgate parking spots
         return self.tailgate

    def isFull(self):   # True if parking lot has no more available parking spots
         return self.parking == 0 and self.tailgate == 0

    def getDistance(self):
         pass
         # Needs integration with Google Maps API to calculate distance from Event. Using self.address and self.event.getAddress()


class Attendant(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    parkingLot = models.ForeignKey(ParkingLot, null=True, on_delete=models.RESTRICT, help_text="Parking Lot to which this attendant is assigned")
    owner = models.ForeignKey(Owner, help_text="Owner of above parking lot",  on_delete=models.RESTRICT)
