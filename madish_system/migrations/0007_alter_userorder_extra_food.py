# Generated by Django 4.1.3 on 2022-12-05 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madish_system', '0006_alter_userorder_extra_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userorder',
            name='extra_food',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Extra Food'),
        ),
    ]