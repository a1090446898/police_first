from django.shortcuts import render
from django.views.generic.base import View

from .models import Communication, StudyGarden

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


# 学习园地列表
class StudyGardenList(View):
    def get(self, request):
        # 进行选项
        option = request.GET.get('option', '')

        if option == '1' or option == '':
            lists = StudyGarden.objects.all().order_by('-add_time')

        # 进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(lists, 10, request=request)

        lists = p.page(page)

        return render(request, 'study_garden_list.html', {
            'name': '学习园地',
            'lists': lists,
            'option': option,
        })


# 经验交流列表
class CommunicationList(View):
    def get(self, request):
        # 进行选项
        option = request.GET.get('option', '')

        if option == '1' or option == '':
            lists = Communication.objects.all().order_by('-add_time')

        # 进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(lists, 10, request=request)

        lists = p.page(page)

        return render(request, 'communication_list.html', {
            'name': '经验交流',
            'lists': lists,
            'option': option,
        })


# 经验交流详情页
class CommunicationDetails(View):
    def get(self, request, detail_id):
        new_detail = Communication.objects.get(id=int(detail_id))
        new_detail.read_volume += 1
        new_detail.save()
        return render(request, 'detail.html', {
            'new_detail': new_detail,
        })


# 学习园地详情页
class StudyGardenDetails(View):
    def get(self, request, detail_id):
        new_detail = StudyGarden.objects.get(id=int(detail_id))
        new_detail.read_volume += 1
        new_detail.save()
        return render(request, 'detail.html', {
            'new_detail': new_detail,
        })
