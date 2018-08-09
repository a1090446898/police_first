# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-07-28 11:18
from __future__ import unicode_literals

import DjangoUeditor.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuildWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('content', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
                ('read_volume', models.IntegerField(default=0, verbose_name='阅读量')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.Source', verbose_name='文章来源')),
            ],
            options={
                'verbose_name': '党建工作',
                'verbose_name_plural': '党建工作',
            },
        ),
        migrations.CreateModel(
            name='HelpNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('content', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
                ('read_volume', models.IntegerField(default=0, verbose_name='阅读量')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.Source', verbose_name='文章来源')),
            ],
            options={
                'verbose_name': '协助破案',
                'verbose_name_plural': '协助破案',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='banner/%Y/%m', verbose_name='轮播图')),
                ('is_banner', models.BooleanField(default=False, verbose_name='是否轮播')),
                ('content', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
                ('read_volume', models.IntegerField(default=0, verbose_name='阅读量')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.Source', verbose_name='文章来源')),
            ],
            options={
                'verbose_name': '监管要闻',
                'verbose_name_plural': '监管要闻',
            },
        ),
        migrations.CreateModel(
            name='PlacesNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('content', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
                ('read_volume', models.IntegerField(default=0, verbose_name='阅读量')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.Source', verbose_name='文章来源')),
            ],
            options={
                'verbose_name': '各地动态',
                'verbose_name_plural': '各地动态',
            },
        ),
        migrations.CreateModel(
            name='TeamNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('content', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
                ('read_volume', models.IntegerField(default=0, verbose_name='阅读量')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.Source', verbose_name='文章来源')),
            ],
            options={
                'verbose_name': '支队动态',
                'verbose_name_plural': '支队动态',
            },
        ),
        migrations.CreateModel(
            name='VideoPatrol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('content', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
                ('read_volume', models.IntegerField(default=0, verbose_name='阅读量')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.Source', verbose_name='文章来源')),
            ],
            options={
                'verbose_name': '视频巡查',
                'verbose_name_plural': '视频巡查',
            },
        ),
    ]