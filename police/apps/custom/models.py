from datetime import datetime

from django.db import models


# Create your models here.


class LogoImage(models.Model):
    title = models.CharField(max_length=30, verbose_name='标题', default='')
    image = models.ImageField(upload_to='logo/%Y/%m', verbose_name='Logo', max_length=100, blank=True, null=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = 'Logo'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class MovieWindow(models.Model):
    title = models.CharField(max_length=30, verbose_name='标题', default='')
    image = models.ImageField(upload_to='window/%Y/%m', verbose_name='Logo', max_length=100, blank=True, null=True)
    # is_window = models.BooleanField(default=True, verbose_name='是否开启飘窗')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '飘窗'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class OtherConnections(models.Model):
    title = models.CharField(max_length=30, verbose_name='标题', default='')
    url = models.URLField(max_length=200, verbose_name='访问连接')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '各所链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

