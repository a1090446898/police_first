# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-07-28 11:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='communication',
            name='is_imgText',
            field=models.BooleanField(default=False, verbose_name='是否是图文'),
        ),
        migrations.AddField(
            model_name='studygarden',
            name='is_imgText',
            field=models.BooleanField(default=False, verbose_name='是否是图文'),
        ),
    ]
