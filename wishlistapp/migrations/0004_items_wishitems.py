# Generated by Django 3.1.1 on 2020-09-05 13:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wishlistapp', '0003_auto_20200905_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('info', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WishItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wishlistapp.items')),
                ('wishlist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wishlistapp.wish')),
            ],
        ),
    ]
