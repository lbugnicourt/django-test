# Generated by Django 3.2.5 on 2022-10-16 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geography', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusStop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_time', models.DateTimeField(verbose_name='Time to reach bus stop')),
                ('passenger_number', models.IntegerField(verbose_name='Number of passenger to pickup')),
            ],
        ),
    ]
