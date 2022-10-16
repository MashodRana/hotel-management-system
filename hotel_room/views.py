from django.shortcuts import render
from django.views import View

# Create your views here.
class RoomsView(View):
    template_name = 'pages/rooms.html'

    def get(self, req, *args, **kwargs):
        return render(req, self.template_name, context={'rooms':'All romms'})