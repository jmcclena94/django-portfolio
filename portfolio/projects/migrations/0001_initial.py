# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-11 06:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.ImageField(upload_to='covers/')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date_completed', models.DateField()),
                ('url', models.URLField(max_length=255)),
                ('github', models.URLField(max_length=255)),
            ],
        ),
    ]
