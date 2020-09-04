from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='wishlistapp/index.html')),
    path('accounts/', include('allauth.urls')),
    path('', include('wishlistapp.urls')),
]
