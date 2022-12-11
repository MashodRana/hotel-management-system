from http.client import HTTPResponse
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.
class HomeView(View):
    template_name = 'pages/home_page.html'
    def get(self, request, *args, **kwargs):
        context = {
            'title': 'MR Palace',
            'active_nav_item': 'nav-home'
        }
        return render(request, self.template_name, context=context)


class ContactView(View):
    template_name = 'pages/contact.html'

    def get(self, request, *args, **kwargs):
        context = {
            'title': 'Conatct',
            'active_nav_item': 'nav-contact'
        }
        return render(request, self.template_name, context=context)


class AboutView(View):
    template_name = 'pages/about.html'

    def get(self, request, *args, **kwargs):
        context = {
            'title': 'About',
            'active_nav_item': 'nav-about'
        }
        return render(request, self.template_name, context=context)