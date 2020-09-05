from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Wish, Item, WishItem


def home(request):
    context = {
        'posts': Wish.objects.all()
    }
    return render(request, 'wishlistapp/home.html', context)


class WishListView(ListView):
    model = Wish
    template_name = 'wishlistapp/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class WishDetailView(DetailView):
    model = Wish


class WishCreateView(LoginRequiredMixin, CreateView):
    model = Wish
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class WishUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Wish
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class WishDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Wish
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def items(request):
    context = {
        'items': Item.object.all()
    }
    return render(request, 'wishlistapp/items.html', context)


def wishlist(request):

    if request.user.is_authenticated:
        wish, created = Wish.objects.get_or_create(author=request.user)
        item = wish.wishitem_set.all()
    else:
        item = []

    context = {
        'wishitems': item
    }

    return render(request, 'wishlistapp/wishitems.html', context)


class ItemListView(ListView):
    model = Item
    template_name = 'wishlistapp/items.html'
    context_object_name = 'items'


class ItemDetailView(DetailView):
    model = Item


def about(request):
    return render(request, 'wishlistapp/about.html', {'title': 'About'})

