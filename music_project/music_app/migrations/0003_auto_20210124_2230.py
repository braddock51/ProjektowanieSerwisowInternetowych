# Generated by Django 2.2.12 on 2021-01-24 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0002_auto_20210124_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=10000),
        ),
    ]