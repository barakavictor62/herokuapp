# Generated by Django 2.0 on 2017-12-30 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popeye', '0004_auto_20171225_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitebuilding',
            name='title',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
