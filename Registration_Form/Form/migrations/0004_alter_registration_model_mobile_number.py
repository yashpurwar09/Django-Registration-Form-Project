# Generated by Django 5.1.2 on 2024-10-26 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0003_alter_registration_model_mobile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration_model',
            name='mobile_number',
            field=models.CharField(max_length=10),
        ),
    ]
