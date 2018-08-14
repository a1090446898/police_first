from django.conf.urls import url, include


from .views import *

urlpatterns = [
    url(r'^communication/$', CommunicationList.as_view(), name='communication_list'),
    url(r'^study_garden/$', StudyGardenList.as_view(), name='study_garden_list'),

    url(r'^communication_detail/(?P<detail_id>\d+)$', CommunicationDetails.as_view(), name='communication_detail'),
    url(r'^study_garden_detail/(?P<detail_id>\d+)$', StudyGardenDetails.as_view(), name='study_garden_detail'),

]