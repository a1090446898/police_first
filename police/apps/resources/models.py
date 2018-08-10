from datetime import  datetime

from django.db import models

# Create your models here.


class Resources(models.Model):
    title = models.CharField(max_length=100, verbose_name='业务名')
    download = models.FileField(upload_to='resource/%Y/%m', verbose_name='资源文件', max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '业务资源'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
