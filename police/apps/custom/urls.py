from django.conf.urls import url, include
from .views import DutyView


urlpatterns = [
    url(r'^duty/', DutyView.as_view(), name='duty'),

]
