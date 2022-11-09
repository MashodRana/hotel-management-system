from django.shortcuts import render, redirect
from django.views import View

from user_profile.models import Person
from user_profile.forms import PersonForm

# Create your views here.
class RegisterView(View):
    template_name = 'user/register.html'
    
    def get(self, request, *args, **kwargs):
        person_form = PersonForm()
        print(type(person_form))
        return render(request, self.template_name, context={'form':person_form, 'name':"mashod"})
    
    def post(self, request, *args, **kwargs):
        return redirect('home')