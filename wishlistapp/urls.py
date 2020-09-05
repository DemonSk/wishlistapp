from django.urls import path
from .views import WishListView, WishDetailView, WishCreateView, WishUpdateView, WishDeleteView
from . import views

urlpatterns = [
    path('', WishListView.as_view(), name='wishlist-home'),
    path('wishlist/<int:pk>', WishDetailView.as_view(), name='wishlist-detail'),
    path('wishlist/new/', WishCreateView.as_view(), name='wishlist-create'),
    path('wishlist/<int:pk>/update/', WishUpdateView.as_view(), name='wishlist-update'),
    path('wishlist/<int:pk>/delete/', WishDeleteView.as_view(), name='wishlist-delete'),
    path('about/', views.about, name='wishlist-about')


]