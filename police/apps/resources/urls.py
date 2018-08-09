from django.conf.urls import url, include


from .views import ResourcesList


urlpatterns = [
    url(r'^$', ResourcesList.as_view(), name='list'),

]