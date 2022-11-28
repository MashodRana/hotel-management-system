from django.db import models
from django.contrib.auth import get_user_model

from user_profile.models import Person
from hotel_room.models import Room

# Create your models here.
class Booking(models.Model):
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
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    booking_status = models.CharField(max_length=50, choices=BOOKING_STATUS)
    check_in = models.DateTimeField(blank=True, null=True)
    check_out = models.DateTimeField(blank=True, null=True)
    room_cleaning = models.BooleanField(default=False)
    laundry = models.BooleanField(default=False)
    breakfast = models.BooleanField(default=False)

class WishList(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    check_in = models.DateTimeField(blank=True, null=True)
    check_out = models.DateTimeField(blank=True, null=True)
    room_cleaning = models.BooleanField(default=False)
    laundry = models.BooleanField(default=False)
    breakfast = models.BooleanField(default=False)
    total_price = models.FloatField(default=0)

    def __str__(self):
        return f"{self.room.room_number} {self.room.style}"



