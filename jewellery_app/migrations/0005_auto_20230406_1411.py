# Generated by Django 3.2.18 on 2023-04-06 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewellery_app', '0004_auto_20230406_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to='slider/img1/'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='slider/img2/'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to='slider/img3/'),
        ),
    ]