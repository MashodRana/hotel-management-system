from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.RoomsView.as_view(), name="rooms" ),
    path('standard/', views.get_standard_rooms, name='standard_rooms'),
    path('delux/', views.get_delux_rooms, name='delux_rooms'),
    path('suit/', views.get_suit_rooms, name='suit_rooms'),
    path('apartment/', views.get_apartment_rooms, name='apartment_rooms'),
]