from django.contrib import admin

from room_booking.models import Booking, WishList, BookingHistroy


# Register your models here.
admin.site.register(Booking)
admin.site.register(WishList)
admin.site.register(BookingHistroy)