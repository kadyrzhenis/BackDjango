# Generated by Django 3.1.7 on 2021-03-06 00:07

import auth_.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_', '0002_mainuser_is_staff'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='mainuser',
            managers=[
                ('objects', auth_.models.MainUserManager()),
            ],
        ),
    ]
