# Generated by Django 4.0.8 on 2022-11-25 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mundial', '0008_user_password'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Account',
        ),
    ]
