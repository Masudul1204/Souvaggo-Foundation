# Generated by Django 5.0.1 on 2024-01-24 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0004_sub_home_insert'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sub_home_insert',
            name='title',
        ),
    ]