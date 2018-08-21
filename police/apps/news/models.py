from datetime import datetime

from django.db import models

from DjangoUeditor.models import UEditorField
from apps.work.models import Source


class News(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    introduce = models.CharField(max_length=50, verbose_name='简介', default='')
    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name='轮播图',
                              max_length=100, default='', null=True, blank=True)
    is_banner = models.BooleanField(default=False, verbose_name='是否轮播')
    content = UEditorField(verbose_name='内容', width=1100, height=600, imagePath='news/images/%(basename)s_%(datetime)s.%(extname)s',
                           filePath='news/images/%(basename)s_%(datetime)s.%(extname)s', default='')
    source = models.ForeignKey(Source, verbose_name='文章来源')
    read_volume = models.IntegerField(default=0, verbose_name='阅读量')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '监管要闻'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class BannerNews(News):
    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name
        proxy = True


class TeamNews(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    content = UEditorField(verbose_name='内容', width=1100, height=600, imagePath='teamNews/images/%(basename)s_%(datetime)s.%(extname)s',
                           filePath='teamNews/images/%(basename)s_%(datetime)s.%(extname)s', default='')
    source = models.ForeignKey(Source, verbose_name='文章来源')
    read_volume = models.IntegerField(default=0, verbose_name='阅读量')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '支队动态'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class PlacesNews(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    content = UEditorField(verbose_name='内容', width=1100, height=600, imagePath='placesNews/images/%(basename)s_%(datetime)s.%(extname)s',
                           filePath='placesNews/images/%(basename)s_%(datetime)s.%(extname)s', default='')
    source = models.ForeignKey(Source, verbose_name='文章来源')
    read_volume = models.IntegerField(default=0, verbose_name='阅读量')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '各地动态'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class HelpNews(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    content = UEditorField(verbose_name='内容', width=1100, height=600, imagePath='helpNews/images/%(basename)s_%(datetime)s.%(extname)s',
                           filePath='helpNews/images/%(basename)s_%(datetime)s.%(extname)s', default='')
    source = models.ForeignKey(Source, verbose_name='文章来源')
    read_volume = models.IntegerField(default=0, verbose_name='阅读量')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '协助破案'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class VideoPatrol(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    content = UEditorField(verbose_name='内容', width=1100, height=600, imagePath='videoPatrol/images/%(basename)s_%(datetime)s.%(extname)s',
                           filePath='videoPatrol/images/%(basename)s_%(datetime)s.%(extname)s', default='')
    source = models.ForeignKey(Source, verbose_name='文章来源')
    read_volume = models.IntegerField(default=0, verbose_name='阅读量')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '视频巡查'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class BuildWork(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    content = UEditorField(verbose_name='内容', width=1100, height=600, imagePath='buildWork/images/%(basename)s_%(datetime)s.%(extname)s',
                           filePath='buildWork/images/%(basename)s_%(datetime)s.%(extname)s', default='')
    source = models.ForeignKey(Source, verbose_name='文章来源')
    read_volume = models.IntegerField(default=0, verbose_name='阅读量')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '党建工作'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Click(models.Model):
    option = models.IntegerField(verbose_name='标记', default=1)
    index_click = models.IntegerField(verbose_name='点击数', default=0)

    class Meta:
        verbose_name = '首页访问量'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '首页访问量'

