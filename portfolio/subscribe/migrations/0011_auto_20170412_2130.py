# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-04-12 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0010_auto_20170412_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emails',
            name='email',
            field=models.EmailField(default='', max_length=255, unique=True),
        ),
    ]
