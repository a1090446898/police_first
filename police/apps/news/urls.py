from django.conf.urls import url, include

from .views import *


urlpatterns = [

    url(r'^news/$', NewsList.as_view(), name='news_list'),
    url(r'^team_news/$', TeamNewsList.as_view(), name='team_news_list'),
    url(r'^places_news/$', PlacesNewsList.as_view(), name='places_news_list'),
    url(r'^help_news/$', HelpNewsList.as_view(), name='help_news_list'),
    url(r'^video_patrol/$', VideoPatrolList.as_view(), name='video_patrol_list'),
    url(r'^build_work/$', BuildWorkList.as_view(), name='build_work_list'),

    url(r'^news_detail/(?P<detail_id>\d+)$', NewsDetails.as_view(), name='news_detail'),
    url(r'^team_news_detail/(?P<detail_id>\d+)$', TeamNewsDetails.as_view(), name='team_news_detail'),
    url(r'^places_news_detail/(?P<detail_id>\d+)$', PlacesNewsDetails.as_view(), name='places_news_detail'),
    url(r'^help_news_detail/(?P<detail_id>\d+)$', HelpNewsDetails.as_view(), name='help_news_detail'),
    url(r'^video_patrol_detail/(?P<detail_id>\d+)$', VideoPatroDetails.as_view(), name='video_patrol_detail'),
    url(r'^build_work_detail/(?P<detail_id>\d+)$', BuildWorkDetails.as_view(), name='build_work_detail'),


]