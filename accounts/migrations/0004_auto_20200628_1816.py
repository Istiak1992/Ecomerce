# Generated by Django 3.0.4 on 2020-06-28 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_emailconfirmed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emailconfirmed',
            old_name='hashKey',
            new_name='activationKey',
        ),
    ]
