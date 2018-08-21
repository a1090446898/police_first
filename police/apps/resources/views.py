from django.shortcuts import render
from django.views.generic.base import View

from .models import Resources
from custom.models import LogoImage

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


class ResourcesList(View):
    def get(self, request):
        # Logo
        logos = LogoImage.objects.all().order_by('-add_time')
        option = request.GET.get('option', '')
        lists = Resources.objects.all().order_by('-add_time')

        # 进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(lists, 9, request=request)

        lists = p.page(page)

        return render(request, 'down_list.html', {
            'name': '资源下载',
            'lists': lists,
            'option': option,
            'logos': logos,

        })
