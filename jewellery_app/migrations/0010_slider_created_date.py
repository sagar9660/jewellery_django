# Generated by Django 3.2.18 on 2023-04-07 05:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jewellery_app', '0009_remove_slider_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]