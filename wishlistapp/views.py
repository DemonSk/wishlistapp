from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'wishlistapp/index.html')


def items(request):
    context = {}
    return render(request, 'wishlistapp/items.html', context)


def wishlist(request):
    context = {}
    return render(request, 'wishlistapp/wishlist.html', context)

