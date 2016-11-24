# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 22:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comprador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=140)),
                ('enlace', models.ManyToManyField(to='app.Enlace')),
            ],
        ),
    ]
