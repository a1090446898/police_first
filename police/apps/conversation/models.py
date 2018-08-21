from datetime import datetime

from django.db import models

from DjangoUeditor.models import UEditorField


# Create your models here.
class Communication(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    content = UEditorField(verbose_name='内容', width=1100, height=600, imagePath='communication/images/%(basename)s_%(datetime)s.%(extname)s',
                           filePath='communication/images/%(basename)s_%(datetime)s.%(extname)s', default='')
    read_volume = models.IntegerField(default=0, verbose_name='阅读量')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '经验交流'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class StudyGarden(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    content = UEditorField(verbose_name='内容', width=1100, height=600, imagePath='study_garden/images/%(basename)s_%(datetime)s.%(extname)s',
                           filePath='study_garden/images/%(basename)s_%(datetime)s.%(extname)s', default='')
    read_volume = models.IntegerField(default=0, verbose_name='阅读量')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '学习园地'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title