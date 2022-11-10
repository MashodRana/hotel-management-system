from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from user_profile.models import Account, Person


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Account
        fields = ('email',)


class PersonForm(forms.ModelForm):
    password = forms.CharField(max_length=12, widget=forms.PasswordInput())
    class Meta:
        model = Person
        fields = '__all__'


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['email', 'password']