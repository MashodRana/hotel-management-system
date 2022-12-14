from http.client import HTTPResponse
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
import json

from root_app.forms import SearchForm


# Create your views here.
class HomeView(View):
    template_name = 'pages/home_page.html'
    def get(self, request, *args, **kwargs):
        context = {
            'title': 'MR Palace',
            'active_nav_item': 'nav-home',
            'search_form': SearchForm()
        }
        return render(request, self.template_name, context=context)

class SearchRoomView(View):
    __template_name = 'pages/search_result.html'

    def get(self, request, *args, **kwargs):
        print(request.GET)
        form = SearchForm(request.GET)
        if form.is_valid():
            print("uer valid form")
        else:
            context = {
                'title': 'MR Palace',
                'active_nav_item': 'nav-home',
                'search_form': form
            }
            return render(request, self.template_name, context=context)

        context = {
            'title': 'Search Result',
            'active_nav_item': 'nav-home'
        }
        return render(request=request, template_name=self.__template_name, context=context)

    def post(self, request, *args, **kwargs):
        pass


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
    