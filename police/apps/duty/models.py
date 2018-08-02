from datetime import datetime


from django.db import models

# Create your models here.


class Duty(models.Model):
    week = models.IntegerField(choices=((0, '星期一'), (1, '星期二'), (2, '星期三')
                                        , (3, '星期四'), (4, '星期五'), (5, '星期六')
                                        , (6, '星期天')), default=1
                               , verbose_name='值班星期')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '值班日期'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}-{1}'.format(self.week, self.time)


class DutyMan(models.Model):
    time = models.ForeignKey(Duty, verbose_name='值班时间')
    type = models.CharField(choices=(('ld', '领导'), ('mj', '民警')),
                            max_length=10, verbose_name='类型', default='ld')
    name = models.CharField(max_length=10, verbose_name='姓名')
    telephone = models.CharField(max_length=11, verbose_name='值班电话')
    phone = models.CharField(max_length=11, verbose_name='移动手机')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '值班人'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
