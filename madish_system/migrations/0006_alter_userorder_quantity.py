# Generated by Django 4.0.6 on 2022-12-06 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madish_system', '0005_foodmenu_with_extra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userorder',
            name='quantity',
            field=models.CharField(max_length=255, verbose_name='Quantity'),
        ),
    ]