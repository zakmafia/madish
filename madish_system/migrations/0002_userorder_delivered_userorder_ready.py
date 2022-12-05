# Generated by Django 4.1.3 on 2022-12-05 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madish_system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userorder',
            name='delivered',
            field=models.BooleanField(default=False, verbose_name='Delivered'),
        ),
        migrations.AddField(
            model_name='userorder',
            name='ready',
            field=models.BooleanField(default=False, verbose_name='Ready'),
        ),
    ]