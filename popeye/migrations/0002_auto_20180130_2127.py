# Generated by Django 2.0.1 on 2018-01-30 18:27

from django.db import migrations, models
import popeye.models


class Migration(migrations.Migration):

    dependencies = [
        ('popeye', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to=popeye.models.upload_to),
        ),
    ]
