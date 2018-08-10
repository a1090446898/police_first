from datetime import datetime


from django.db import models

# Create your models here.


class DutyMan(models.Model):
    time = models.IntegerField(choices=((0, '星期一'), (1, '星期二'), (2, '星期三')
                                        , (3, '星期四'), (4, '星期五'), (5, '星期六')
                                        , (6, '星期天')), default=0, verbose_name='值班星期')
    leader = models.CharField(max_length=10, verbose_name='领导')
    leader_phone = models.CharField(max_length=11, verbose_name='移动手机')
    follower = models.CharField(max_length=10, verbose_name='民警')
    telephone = models.CharField(max_length=11, verbose_name='值班电话')
    follower_phone = models.CharField(max_length=11, verbose_name='移动手机')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '值班人'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
