from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Item(models.Model):
    name = models.CharField(max_length=50)
    info = models.CharField(max_length=100)
    image = models.ImageField(default='defaulf.jpg', upload_to='item_pics')

    def __str__(self):
        return self.name


class Wish(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('wishlist-detail', kwargs={'pk': self.pk})


class WishItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True)
    wishlist = models.ForeignKey(Wish, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)







