# Generated by Django 4.1.3 on 2022-12-05 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madish_system', '0007_alter_userorder_extra_food'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodmenu',
            name='with_extra',
            field=models.BooleanField(default=False, verbose_name='With Extra'),
        ),
    ]
