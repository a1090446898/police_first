# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-08-15 21:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0005_duty'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='duty',
            options={'verbose_name': '值日表', 'verbose_name_plural': '值日表'},
        ),
    ]
