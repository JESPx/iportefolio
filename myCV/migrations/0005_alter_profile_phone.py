# Generated by Django 4.2.5 on 2023-09-06 15:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCV', '0004_remove_profile_age_alter_profile_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='Phone number can only contain digits.', regex='^\\d+$')]),
        ),
    ]
