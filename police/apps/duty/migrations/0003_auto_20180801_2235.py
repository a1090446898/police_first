# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-08-01 22:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duty', '0002_auto_20180801_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duty',
            name='week',
            field=models.IntegerField(choices=[(0, '星期一'), (1, '星期二'), (2, '星期三'), (3, '星期四'), (4, '星期五'), (5, '星期六'), (6, '星期天')], default=1, verbose_name='值班星期'),
        ),
    ]