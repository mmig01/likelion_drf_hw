# Generated by Django 5.0.6 on 2024-07-02 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singer',
            name='debut',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='song',
            name='release',
            field=models.DateTimeField(),
        ),
    ]