# Generated by Django 4.0.8 on 2022-11-14 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mundial', '0006_match_rename_result_bet_bet_result_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
