from datetime import datetime


from django.db import models

# Create your models here.


class Plate(models.Model):
    name = models.CharField(choices=(('jg', '监管要闻'), ('gd', '各地动态')), verbose_name='投稿板块',
                            default='jg', max_length=10)

    class Meta:
        verbose_name = '投稿板块'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Submission(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    plate = models.CharField(choices=(('jg', '监管要闻'), ('gd', '各地动态')), verbose_name='投稿板块'
                             ,default='jg', max_length=10)
    name = models.CharField(max_length=10, verbose_name='姓名')
    phone = models.CharField(max_length=11, verbose_name='手机号')
    address = models.CharField(max_length=150, verbose_name='地址')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    is_read = models.BooleanField(verbose_name='是否阅读', default=False)
    is_pass = models.BooleanField(verbose_name='是否审核通过', default=False)
    is_imgText = models.BooleanField(default=False, verbose_name='是否是图文')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '投稿'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
