# Generated by Django 4.1.7 on 2023-03-14 07:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_imagslid'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagslid',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
