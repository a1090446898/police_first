from django.conf.urls import url, include

from .views import SubmissionAsk, SuccessView


urlpatterns = [
    url(r'^$', SubmissionAsk.as_view(), name='formAsk'),
    url(r'^form_submission/$', SubmissionAsk.as_view(), name='form_submission'),
    url(r'^success/$', SuccessView.as_view(), name='success'),

]
