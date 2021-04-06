from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Profile(models.Model):  # Set up a profile to attach to a user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userType = models.TextField(max_length=500, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Event(models.Model):
    name = models.CharField(max_length=50, help_text="The long name of the event, with spaces")
    shortName = models.CharField(max_length=15,
                                 help_text="Short event name, used when creating attendant 'email' addresses")
    date = models.DateTimeField("Date", default=timezone.now)
    #manager = models.ForeignKey(Manager, help_text="Manager who created the Event", on_delete=models.CASCADE)
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
    #owner = models.ForeignKey(Owner, on_delete=models.CASCADE, help_text="Owner of the parking lot")
    event = models.ManyToManyField(Event, help_text="Event(s) that will use this parking lot")
    date = models.DateField(help_text="Date of the Event")
    # distance = getDistance()
    price = models.DecimalField(max_digits=5, decimal_places=2, help_text="Cost of a normal parking spot", default=20.00)
    tailgatePrice = models.DecimalField(max_digits=5, decimal_places=2, help_text="Cost of a tailgate parking spot", default=30.00)

    class Meta:
        ordering = ['date', 'price', 'tailgatePrice']

    def __str__(self):  # Useful for printing out Name and Address of the parking lot
        return "%s \n %s" % (self.name, self.address)
        # return [self.name, self.address]  # If we find this works better for our purposes.

    def availSpots(self):  # Get the number of available normal parking spots
        return self.parking

    def availTailgate(self):  # Get the number of available tailgate parking spots
        return self.tailgate

    def isFull(self):  # True if parking lot has no more available parking spots
        return self.parking == 0 and self.tailgate == 0

    def getDistance(self):
        pass
        # Needs integration with Google Maps API to calculate distance from Event. Using self.address and self.event.getAddress()