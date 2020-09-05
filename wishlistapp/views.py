from django.shortcuts import render
from .models import Wish


def home(request):
    context = {
        'posts': Wish.objects.all()
    }
    return render(request, 'wishlistapp/home.html', context)


def about(request):
    return render(request, 'wishlistapp/about.html')

