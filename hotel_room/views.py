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

class RoomDetailsView(View):
    template_name = "pages/room_details.html"

    ROOM_STATUS = (

        ("available", "Available"),
        ("resersved", "Resersved"),
        ("occupied", "Occupied"),
        ("not available", "Not Available"),
        ("being serviced", "Being Serviced"),
        ("other", "Other")
    )

    def get(self, req, *args, **kwargs):
        room_number = 201
        room_details = Room.objects.get(room_number=room_number)
        
        return render(req, self.template_name, context={"room_details":room_details})
       
@require_GET
def get_standard_rooms(req):
    filtered_rooms = Room.objects.filter(style='standard').values()
    return JsonResponse({'filtered_rooms':list(filtered_rooms)})

@require_GET
def get_delux_rooms(req):
    delux_rooms = Room.objects.filter(style='delux').values()
    return JsonResponse({'filtered_rooms':list(delux_rooms)})

@require_GET
def get_family_suit(req):
    filtered_rooms = Room.objects.filter(style='family').values()
    return JsonResponse({'filtered_rooms':list(filtered_rooms)})

@require_GET
def get_business_suit(req):
    filtered_rooms = Room.objects.filter(style='business').values()
    return JsonResponse({'filtered_rooms':list(filtered_rooms)})

