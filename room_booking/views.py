from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class WishListView(LoginRequiredMixin, View):
    __template_name = 'room_booking/wishlist.html'
    # login_url = ''

    def post(self, request, *args, **kwargs):
        print(request)
        print(request.user)
        return JsonResponse({"msg": "Added to wish list."})
    def get(self, request, *args, **kwargs):
        pass
