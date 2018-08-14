from datetime import datetime


from django.db import models

# Create your models here.


class Submission(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    name = models.CharField(max_length=10, verbose_name='姓名')
    phone = models.CharField(max_length=11, verbose_name='手机号')
    address = models.CharField(max_length=150, verbose_name='地址')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    is_read = models.BooleanField(verbose_name='是否阅读', default=False)
    is_pass = models.BooleanField(verbose_name='是否审核通过', default=False)
    read_volume = models.IntegerField(default=0, verbose_name='阅读量')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '待审核'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class SubmissionPass(Submission):
    class Meta:
        verbose_name = '审核通过'
        verbose_name_plural = verbose_name
        proxy = True


class SubmissionRead(Submission):
    class Meta:
        verbose_name = '审核未通过'
        verbose_name_plural = verbose_name
        proxy = True
