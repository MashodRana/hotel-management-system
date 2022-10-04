from pyexpat import model
from random import choices
from django.db import models


# Create your models here.
class Hotel(models.Model):
    name: models.CharField = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.name


class Room(models.Model):
    ROOM_STYLE = (
        ('standard', 'Standard'),
        ("delux", "Delux"),
        ("family suite", "Family Suite"),
        ("business suite", "Business Suite")
    )
    ROOM_STATUS = (

        ("available", "Available"),
        ("resersved", "Resersved"),
        ("occupied", "Occupied"),
        ("not available", "Not Available"),
        ("being serviced", "Being Serviced"),
        ("other", "Other")
    )

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10, unique=True)
    style = models.CharField(max_length=20, choices=ROOM_STYLE)
    room_status = models.CharField(max_length=30, choices=ROOM_STATUS)
    booking_price = models.IntegerField()
    is_smoking = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.room_number
    

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
    start_date = models.DateTimeField()
    duration_in_days = models.SmallIntegerField()
    status = models.CharField(max_length=50, choices=BOOKING_STATUS)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    