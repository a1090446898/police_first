# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-08-12 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0005_auto_20180812_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testsub',
            name='content',
            field=models.TextField(max_length=100, verbose_name='内容'),
        ),
    ]