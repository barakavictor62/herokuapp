# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-20 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popeye', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=255),
        ),
    ]