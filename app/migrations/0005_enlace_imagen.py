# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20160930_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='enlace',
            name='imagen',
            field=models.ImageField(default='enlaces/None/no-img.jpg', upload_to='enlaces/'),
        ),
    ]
