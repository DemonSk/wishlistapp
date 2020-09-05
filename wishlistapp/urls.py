from django.urls import path
from .views import (
    WishListView,
    WishDetailView,
    WishCreateView,
    WishUpdateView,
    WishDeleteView,
    ItemListView,
    ItemDetailView)
from . import views

urlpatterns = [
    path('', WishListView.as_view(), name='wishlist-home'),
    path('wishlist/<int:pk>', WishDetailView.as_view(), name='wishlist-detail'),
    path('wishlist/new/', WishCreateView.as_view(), name='wishlist-create'),
    path('wishlist/<int:pk>/update/', WishUpdateView.as_view(), name='wishlist-update'),
    path('wishlist/<int:pk>/delete/', WishDeleteView.as_view(), name='wishlist-delete'),
    path('items/', ItemListView.as_view(), name='items'),
    path('items/<int:pk>', ItemDetailView.as_view(), name='items-detail'),
    path('wishlist/wishitems/', views.wishlist, name='wishitems'),
    path('about/', views.about, name='wishlist-about')


]