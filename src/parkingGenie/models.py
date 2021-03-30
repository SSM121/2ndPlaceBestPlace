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

    userType = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)
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
     user = models.OneToOneField(Account, on_delete=models.CASCADE)

     carMake = models.CharField(max_length=15, help_text="Make of the customers car")
     carModel = models.CharField(max_length=15, help_text="Model of the customers car")
     carColor = models.CharField(max_length=15, help_text="Color of the customers car")
     carPlate = models.CharField(max_length=15, help_text="Licence plate of the customers car")

#     class Meta:
#        permissions = ['customer']
#
#
class Owner(models.Model):
     user = models.OneToOneField(Account, on_delete=models.CASCADE)
     parkingLots = models.JSONField(null=True, help_text="List of this owners parking lots")

#     class Meta:
#         permissions = ['owner']
#
#
class Manager(models.Model):
     user = models.OneToOneField(Account, on_delete=models.CASCADE)

#     class Meta:
#         permissions = ['manager']
#
#
class Attendant(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    #parkingLot = models.ForeignKey(ParkingLot, help_text="Parking Lot to which this attendant is assigned") # Need PL
    owner = models.ForeignKey(Owner, help_text="Owner of above parking lot",  on_delete=models.CASCADE)
#
#     class Meta:
#         permissions = ['attendant']
#
class Event(models.Model):
     name = models.CharField(max_length=50, help_text="The long name of the event, with spaces")
     shortName = models.CharField(max_length=15, help_text="Short event name, used when creating attendant 'email' addresses")
     date = models.DateField
     manager = models.ForeignKey(Manager, help_text="Manager who created the Event", on_delete=models.CASCADE)
     address = models.CharField(max_length=100, help_text="Address of the Event")
#
#     class Meta:
#         ordering = ["date"]

     def __str__(self):
         return "%s \n %s" % (self.name, self.address)

     def getShortName(self):
         return self.shortName

     def getAddress(self):
         return self.address


class ParkingLot(models.Model):
#
#     class Meta:
#         ordering = ["date", "distance", "price", "tailgatePrice"]
#
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


     # Fields
     name = models.CharField(max_length=20, help_text="The name of the parking lot")
     address = models.CharField(max_length=100, help_text="Address of the parking lot")
     parking = models.IntegerField(help_text="Number of available normal parking spaces")
     tailgate = models.IntegerField(help_text="Number of available tailgate parking spaces")
     owner = models.ForeignKey(Owner, on_delete=models.CASCADE, help_text="Owner of the parking lot")
     event = models.ManyToManyField(Event, help_text="Event(s) that will use this parking lot")
     date = models.DateField(help_text="Date of the Event")
     #distance = getDistance()  # IDK how to fix this but it needs an argument of "Self"
     price = models.DecimalField(max_digits=5, decimal_places=2, help_text="Cost of a normal parking spot", default=20.00)
     tailgatePrice = models.DecimalField(max_digits=5, decimal_places=2, help_text="Cost of a tailgate parking spot", default=30.00)



