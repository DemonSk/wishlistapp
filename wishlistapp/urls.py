from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='wishlist-home'),
    path('items/', views.items, name='items'),
    path('wishlist/', views.wishlist, name='wishlist'),

]