"""police URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from apscheduler.schedulers.background import BackgroundScheduler

import xadmin
from news.views import IndexView
from custom.views import IntroduceView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^news/', include('news.urls', namespace='news')),
    url(r'^work/', include('work.urls', namespace='work')),
    url(r'^resources/', include('resources.urls', namespace='resources')),
    url(r'^conversation/', include('conversation.urls', namespace='conversation')),
    url(r'^operation/', include('operation.urls', namespace='operation')),
    url(r'^custom/', include('custom.urls', namespace='custom')),


    url(r'^$', IndexView.as_view(), name='Index'),
    url(r'^introduce/$', IntroduceView.as_view(), name='introduce'),


    # 配置上传文件访问处理
    url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
    # 静态文件访问路径
    # url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

]


# 全局404，500的配置
handler404 = 'work.views.page_not_found'
handler500 = 'work.views.page_error'

# 定时函数
# sched = BackgroundScheduler()
#
#
# def test1():
#     print('时间运行了')
#
#
# sched.add_job(test1, 'cron', day='*', hour='*', minute='*', second='*')
# sched.start()
