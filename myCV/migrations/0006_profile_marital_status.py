# Generated by Django 4.2.5 on 2023-09-06 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCV', '0005_alter_profile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='marital_status',
            field=models.CharField(choices=[('veuf', 'Veuf'), ('marié', 'Marié'), ('célibataire', 'Célibataire')], default='célibataire', max_length=20),
        ),
    ]