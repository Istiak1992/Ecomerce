# Generated by Django 3.0.4 on 2020-07-02 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200628_1816'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emailconfirmed',
            old_name='activationKey',
            new_name='activation_key',
        ),
    ]
