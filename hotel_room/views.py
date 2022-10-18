from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.decorators.http import require_GET

from .models import Room

# Create your views here.
class RoomsView(View):
    template_name = 'pages/rooms.html'

    def get(self, req, *args, **kwargs):
        rooms = Room.objects.all()
        return render(req, self.template_name, context={'rooms':rooms})


@require_GET
def get_standard_rooms(req):
    standard_rooms = Room.objects.filter(style='standard').values()
    return JsonResponse({'filtered_rooms':list(standard_rooms)})

@require_GET
def get_delux_rooms(req):
    delux_rooms = Room.objects.filter(style='delux').values()
    return JsonResponse({'filtered_rooms':list(delux_rooms)})

@require_GET
def get_suit_rooms(req):
    filtered_rooms = Room.objects.filter(style='suit').values()
    return JsonResponse({'filtered_rooms':list(filtered_rooms)})

@require_GET
def get_apartment_rooms(req):
    filtered_rooms = Room.objects.filter(style='apartment').values()
    return JsonResponse({'filtered_rooms':list(filtered_rooms)})