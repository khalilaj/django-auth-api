# Generated by Django 2.0.5 on 2018-12-09 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20181207_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='session_image',
            field=models.FileField(blank=True, upload_to='', verbose_name='app-logo'),
        ),
    ]
