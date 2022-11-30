from django.urls import path

from room_booking import views


urlpatterns = [
    path('add-to-wishlist/', views.AddToWishListView.as_view(), name='add_to_wishlist'),
    path('wishlist/', views.WishListView.as_view(), name='wishlist'),

]