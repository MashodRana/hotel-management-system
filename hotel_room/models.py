from email.policy import default
from pyexpat import model
from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models

from user_profile.models import Person


# Create your models here.
class Hotel(models.Model):
    name: models.CharField = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.name


class Room(models.Model):
    ROOM_STYLE = (
        ('standard', 'Standard'),
        ("delux", "Delux"),
        ("family", "Family Suite"),
        ("business", "Business Suite")
    )

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10, unique=True)
    style = models.CharField(max_length=20, choices=ROOM_STYLE)
    booking_price = models.IntegerField()
    is_smoking = models.BooleanField(default=False)
    is_wifi = models.BooleanField(default=False)
    is_ac = models.BooleanField(default=False)
    is_balcony = models.BooleanField(default=False)
    is_tv = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.room_number} {self.style}"
    

class RoomBooking(models.Model):
    BOOKING_STATUS = (
        ("requested", "Requested"),
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("checked-in", "Checked-in"),
        ("checked-out", "Checked-out"),
        ("canceled", "Canceled"),
        ("abandoned", "Abandoned"),
    )
    reservation_number = models.CharField(max_length=20)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    booking_status = models.CharField(max_length=50, choices=BOOKING_STATUS)
    check_in = models.DateTimeField(blank=True, null=True)
    check_out = models.DateTimeField(blank=True, null=True)
    room_cleaning = models.BooleanField(default=False)
    laundry = models.BooleanField(default=False)
    breakfast = models.BooleanField(default=False)


    