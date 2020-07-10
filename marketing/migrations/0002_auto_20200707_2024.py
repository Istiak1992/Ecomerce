# Generated by Django 3.0.4 on 2020-07-07 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('header_text', models.CharField(blank=True, max_length=120, null=True)),
                ('text', models.CharField(blank=True, max_length=120, null=True)),
                ('active', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-start_date', '-end_date'],
            },
        ),
        migrations.AlterModelOptions(
            name='marketingmessage',
            options={'ordering': ['-start_date', '-end_date']},
        ),
    ]
