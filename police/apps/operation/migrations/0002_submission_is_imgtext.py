# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-07-28 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='is_imgText',
            field=models.BooleanField(default=False, verbose_name='是否是图文'),
        ),
    ]
