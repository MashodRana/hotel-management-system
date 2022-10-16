from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.RoomsView.as_view(), name="rooms" ),
]