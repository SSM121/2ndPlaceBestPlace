from django.db import models
from django.urls import reverse  # used to generate URLs by reversing the URL patterns
import uuid  # required for Accounts to have a unique instance


class Account(models.Model):
    # Fields
    accntType = models.CharField(max_length=10, help_text='The type of Account: User, Owner, or Manager')
    name = models.CharField(max_length=40, help_text='Name of the user')
    email = models.EmailField(max_length=254, help_text='Email of the user')
    password = models.CharField(max_length= 15, help_text="The users password")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), help_text="Unique ID for this particular Account")
    # accntInfo = models.JSONField(null=True)

    class Meta:
        ordering = ['email', 'accntType', 'name']

    def __str__(self):  # The __str__ method is useful  so if we want to print out an account we can.
        return self.name.__str__() + " owns an account type of: " + self.accntType.__str__() \
               + ". The email attached to the account is " + self.email.__str__()

    def get_absolute_url(self):  # Not currently implemented Spencer Clemens working through a tutorial
        """ Returns the url to access a detailed record of an account"""
        return reverse('account-detail', args=[str(self.email)])


class ParkingLot(models.Model):
    # Fields
    name = models.CharField(max_length=20, help_text="The name of the parking lot")
    address = models.CharField(max_length=100, help_text="Address of the parking lot")
    parking = models.IntegerField(help_text="Number of available normal parking spaces")
    tailgate = models.IntegerField(help_text="Number of available tailgate parking spaces")
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, help_text="Owner of the parking lot")
    event = models.ManyToManyField(Event, help_text="Event(s) that will use this parking lot")
    date = models.DateField(help_text="Date of the Event")
    distance = getDistance()
    price = models.DecimalField(max_digits=3, decimal_places=2, help_text="Cost of a normal parking spot")
    tailgatePrice = models.DecimalField(max_digits=3, decimal_places=2, help_text="Cost of a tailgate parking spot")

    class Meta:
        ordering = (date, distance, price, tailgatePrice)

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
        # Needs integration with Google Maps API to calculate distance from Event. Using self.address and self.event.getAddress()


class Event(models.Model):
    # Fields
    name = models.CharField(max_length=50, help_text="The long name of the event, with spaces")
    shortName = models.CharField(max_length=15, help_text="Short event name, used when creating attendant 'email' addresses")
    date = models.DateField
    manager = models.ForeignKey(Manager, help_text="Manager who created the Event")
    parking = models.ManyToManyField(ParkingLot, help_text="Parking lots available for this Event")
    address = models.CharField(max_length=100, help_text="Address of the Event")

    class Meta:
        ordering = (date,)

    def __str__(self):
        return "%s \n %s" % (self.name, self.address)

    def getShortName(self):
        return self.shortName

    def getAddress(self):
        return self.address

