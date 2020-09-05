from django.contrib import admin
from .models import Wish, Item, WishItem

admin.site.register(Wish)
admin.site.register(Item)
admin.site.register(WishItem)

