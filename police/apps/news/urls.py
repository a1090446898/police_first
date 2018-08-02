from django.conf.urls import url, include

from .views import NewsDetail


urlpatterns = [
    # url(r'^list/$',)
    url(r'^detail/(?P<new_id>\d+)/$', NewsDetail.as_view(), name='detail'),


]