# Generated by Django 4.1.3 on 2022-11-08 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mundial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='result',
            field=models.CharField(choices=[('1', 1), ('2', 2), ('X', 0)], default='', max_length=1),
        ),
    ]