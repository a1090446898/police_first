from django.conf.urls import url, include

from .views import *


urlpatterns = [
    url(r'^announcement/$', AnnouncementList.as_view(), name='announcement_list'),
    url(r'^work_bulletin/$', WorkBulletinList.as_view(), name='work_bulletin_list'),
    url(r'^notice/$', NoticeList.as_view(), name='notice_list'),
    url(r'^team_system/$', TeamSystemList.as_view(), name='team_system_list'),
    url(r'^laws/$', LawsList.as_view(), name='laws_list'),


    url(r'^announcement_detail/(?P<detail_id>\d+)$', AnnouncementDetails.as_view(), name='announcement_detail'),
    url(r'^work_bulletin_detail/(?P<detail_id>\d+)$', WorkBulletinDetails.as_view(), name='work_bulletin_detail'),
    url(r'^notice_detail/(?P<detail_id>\d+)$', NoticeDetails.as_view(), name='notice_detail'),
    url(r'^team_system_detail/(?P<detail_id>\d+)$', TeamSystemDetails.as_view(), name='team_system_detail'),
    url(r'^laws_detail/(?P<detail_id>\d+)$', LawsDetails.as_view(), name='laws_detail'),
]