# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_categoria_prueba'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='prueba',
            field=models.CharField(default='', max_length=140),
        ),
    ]
