# Generated by Django 3.0.4 on 2020-05-15 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(blank=True, null=True, to='carts.CartItem'),
        ),
    ]
