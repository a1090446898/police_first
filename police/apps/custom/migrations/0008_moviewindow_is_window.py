# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-08-20 22:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0007_duty_detachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviewindow',
            name='is_window',
            field=models.BooleanField(default=True, verbose_name='是否开启飘窗'),
        ),
    ]