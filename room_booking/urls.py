from django.urls import path
from django.contrib.auth.decorators import login_required

from room_booking import views


urlpatterns = [
    path('add-to-wishlist/', login_required(views.WishListView.as_view()), name='add_to_wishlist'),

]