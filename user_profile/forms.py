from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from user_profile.models import Account


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Account
        fields = ('email',)
