from datetime import datetime

from django.db import models


# Create your models here.


class Source(models.Model):
    name = models.CharField(max_length=30, verbose_name='文章来源', default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '文章来源'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Notice(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    source = models.ForeignKey(Source, verbose_name='文章来源')
    read_volume = models.IntegerField(default=0, verbose_name='阅读量')
    is_imgText = models.BooleanField(default=False, verbose_name='是否是图文')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '公示公告'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Announcement(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    source = models.ForeignKey(Source, verbose_name='文章来源')
    read_volume = models.IntegerField(default=0, verbose_name='阅读量')
    is_imgText = models.BooleanField(default=False, verbose_name='是否是图文')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '通知通告'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class WorkBulletin(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    source = models.ForeignKey(Source, verbose_name='文章来源')
    read_volume = models.IntegerField(default=0, verbose_name='阅读量')
    is_imgText = models.BooleanField(default=False, verbose_name='是否是图文')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '工作简报'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class TeamSystem(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    source = models.ForeignKey(Source, verbose_name='文章来源')
    read_volume = models.IntegerField(default=0, verbose_name='阅读量')
    is_imgText = models.BooleanField(default=False, verbose_name='是否是图文')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '支队制度'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Laws(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    source = models.ForeignKey(Source, verbose_name='文章来源')
    read_volume = models.IntegerField(default=0, verbose_name='阅读量')
    is_imgText = models.BooleanField(default=False, verbose_name='是否是图文')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '法律法规'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class SpecialWork(models.Model):
    title = models.CharField(max_length=20, verbose_name='标题')
    data = models.IntegerField(verbose_name='事件数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='更新时间')

    class Meta:
        verbose_name = '专项工作'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

