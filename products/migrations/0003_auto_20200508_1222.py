# Generated by Django 3.0.4 on 2020-05-08 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_sales_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sales_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True),
        ),
    ]
