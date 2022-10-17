from re import I
from django.shortcuts import render
from django.views import View
from .models import Room

# Create your views here.
class RoomsView(View):
    template_name = 'pages/rooms.html'

    def get(self, req, *args, **kwargs):
        rooms = Room.objects.all()
        return render(req, self.template_name, context={'rooms':rooms})