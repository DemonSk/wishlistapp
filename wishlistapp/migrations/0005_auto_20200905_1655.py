# Generated by Django 3.1.1 on 2020-09-05 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlistapp', '0004_items_wishitems'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Items',
            new_name='Item',
        ),
        migrations.RenameModel(
            old_name='WishItems',
            new_name='WishItem',
        ),
    ]