# Generated by Django 4.1.7 on 2023-03-13 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_alter_post_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagSlid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='slid')),
            ],
        ),
    ]
