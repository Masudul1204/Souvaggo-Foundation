# Generated by Django 5.0.1 on 2024-01-22 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_title', models.CharField(max_length=20)),
                ('home_slogan', models.CharField(max_length=50)),
                ('emp_pic', models.ImageField(blank=True, null=True, upload_to='home/')),
            ],
        ),
    ]