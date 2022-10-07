from http.client import HTTPResponse
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.
class HomeView(View):
    template_name = 'pages/home_page.html'
    def get(self, request, *args, **kwargs):
        
        return render(request, self.template_name, context={"name":"mashod"})