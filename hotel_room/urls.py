from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.RoomsView.as_view(), name="rooms" ),
    path('all-single-room/', views.get_all_single_room, name='all_single_room'),
]