from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from user_profile.models import Person, Account
from user_profile.forms import PersonForm, AccountForm, AddressForm, ProfileForm


# Create your views here.
class RegisterView(View):
    template_name = 'user/register.html'
    __homepage_url_name = 'home'
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
            return redirect(self.__homepage_url_name)
        else:
            return render(request, self.template_name, context={'form':form})


class LoginView(View):
    __template_name = 'user/login.html'
    __homepage_url_name = 'home'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # User already logged in
            return redirect(self.__homepage_url_name)
        
        # User not logged in
        return render(request, self.__template_name, context={'form':AccountForm()})
    
    def post(self, request, *args, **kwargs):
        account_form = AccountForm(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect(self.__homepage_url_name)
        else:
            return render(request, self.__template_name, context={'form':AccountForm(), 'error_msg': "Login failed!"})


class LogoutView(View):
    __homepage_url_name = 'home'

    def get(self, request, *args, **kwargs):
        """ Loged out the user """
        logout(request)
        return redirect(self.__homepage_url_name)


class ProfileView(LoginRequiredMixin, View):
    __template_name = 'user/profile.html'

    def get(self, request, *args, **kwargs):
        
        person = Person.objects.get(email=request.user.email)
        context = {
            'person': person
        }

        return render(request=request, template_name=self.__template_name, context=context)


    def post(self, request, *args, **kwargs):
        pass