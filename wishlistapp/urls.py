from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='wishlist-home'),
    path('about/', views.about, name='wishlist-about')


]