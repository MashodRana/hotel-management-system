from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class WishListView(View):
    __template_name = 'room_booking/wishlist.html'

    def post(self, request, *args, **kwargs):
        print(request)
        print(request.user)
        return HttpResponse("User Profile View")
    def get(self, request, *args, **kwargs):
        pass
