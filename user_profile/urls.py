from django.urls import path

from user_profile import views

urlpatterns = [
    path("registration/", views.RegisterView.as_view(), name='registration' ),
]