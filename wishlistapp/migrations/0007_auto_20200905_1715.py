# Generated by Django 3.1.1 on 2020-09-05 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wishlistapp', '0006_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='wish',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wishlistapp.item'),
        ),
        migrations.DeleteModel(
            name='WishItem',
        ),
    ]
