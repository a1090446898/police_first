from django.shortcuts import render
from django.views.generic.base import View
from django.shortcuts import render_to_response
from itertools import chain

from news.models import News
from operation.models import Submission

# Create your views here.


class IndexView(View):
    def get(self, request):
        news = News.objects.all()
        submissions = Submission.objects.filter(is_pass=True)
        return render(request, 'index.html', {
            'Notices': news

        })


def page_not_found(request):
    response = render_to_response('404.html',{})
    response.status_code = 404
    return response


def page_error(request):
    response = render_to_response('500.html',{})
    response.status_code = 500
    return response
