from django.shortcuts import render, redirect
from django.views import View

from user_profile.models import Person, Account
from user_profile.forms import PersonForm

# Create your views here.
class RegisterView(View):
    template_name = 'user/register.html'
    person_role = {
        'admin':False,
        'manager': False,
        'receptionist': False,
        'guest': False,
        'staff': False
    }

    def get(self, request, *args, **kwargs):
        person_form = PersonForm()
        return render(request, self.template_name, context={'form':person_form})
    
    def post(self, request, *args, **kwargs):
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save()
            self.person_role[person.account_type] = True
            account = Account(
                email=person.email,
                is_admin = self.person_role['admin'],
                is_manager = self.person_role['manager'],
                is_receptionist = self.person_role['receptionist'],
                is_guest = self.person_role['guest'],
                is_staff = self.person_role['staff'],
                person=person
            )
            account.set_password(form.cleaned_data.get("password"))
            account.save()
            return redirect('home')
        