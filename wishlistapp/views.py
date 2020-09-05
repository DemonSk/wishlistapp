from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Wish


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


def about(request):
    return render(request, 'wishlistapp/about.html', {'title': 'About'})

