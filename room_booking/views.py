from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
import json
from datetime import datetime

from room_booking.models import WishList, Booking
from user_profile.models import Person
from hotel_room.models import Room


# Create your views here.
class AddToWishListView(LoginRequiredMixin, View):
    __template_name = 'room_booking/wishlist.html'

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        checkin_datetime = datetime.strptime(data['checkInDate'], "%Y-%m-%d").date()
        checkout_datetime = datetime.strptime(data['checkOutDate'], "%Y-%m-%d").date()
        person = Person.objects.get(email=request.user.email)
        room = Room.objects.get(room_number=data["roomNumber"])
        wishlist = WishList(
                            check_in=checkin_datetime,
                            check_out=checkout_datetime,
                            room_cleaning=data["isCleaning"],
                            laundry=data["isLaundry"],
                            breakfast=data["isBreakfast"],
                            total_price=data["totalCost"]
                            )
        wishlist.person = person
        wishlist.room = room
        wishlist.save()
        return JsonResponse({"msg": "Added to wish list."})
    def get(self, request, *args, **kwargs):
        pass


class WishListView(LoginRequiredMixin, View):
    __template_name = 'room_booking/wishlist.html'

    def get(self, request, *args, **kwargs):
        items = WishList.objects.all()

        # Calculate total cost
        total_amount = 0
        for item in items:
            total_amount+=item.total_price
        
        context = {
            'items': items,
            'total_amount': total_amount
        }
        return render(request=request, template_name=self.__template_name, context=context)
    

class DeleteWishListItemView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        WishList.objects.filter(pk=kwargs['id']).delete()
        return redirect("wishlist")


class BookingListView(LoginRequiredMixin, View):
    __template_name="room_booking/my_booking.html"

    def get(self, request, *args, **kwargs):
        context={
            'title':'My Bookings'
        }
        return render(request=request, template_name=self.__template_name, context=context)