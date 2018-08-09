from django.shortcuts import render
from django.views.generic.base import View
from django.shortcuts import render_to_response
from itertools import chain

from news.models import News
from operation.models import Submission
from apps.work.models import *

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


class IndexView(View):
    def get(self, request):
        news = News.objects.all()
        submissions = Submission.objects.filter(is_pass=True)
        return render(request, 'index.html', {
            'Notices': news

        })


# 通知通告列表页
class AnnouncementList(View):
    def get(self, request):
        # 进行选项
        option = request.GET.get('option', '')

        if option == '1' or option == '':
            lists = Announcement.objects.all().order_by('-add_time')
        else:
            lists = Submission.objects.all().order_by('-add_time')

        # 进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(lists, 1, request=request)

        lists = p.page(page)

        return render(request, 'list.html', {
            'name': '通知通告',
            'lists': lists,
            'option': option,

        })


# 工作简报列表页
class WorkBulletinList(View):
    def get(self, request):
        # 进行选项
        option = request.GET.get('option', '')

        if option == '1' or option == '':
            lists = WorkBulletin.objects.all().order_by('-add_time')
        else:
            lists = Submission.objects.all().order_by('-add_time')

        # 进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(lists, 1, request=request)

        lists = p.page(page)

        return render(request, 'work_bulletin_list.html', {
            'name': '工作简报',
            'lists': lists,
            'option': option,

        })


# 公示公告
class NoticeList(View):
    def get(self, request):
        # 进行选项
        option = request.GET.get('option', '')

        if option == '1' or option == '':
            lists = Notice.objects.all().order_by('-add_time')
        else:
            lists = Submission.objects.all().order_by('-add_time')

        # 进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(lists, 1, request=request)

        lists = p.page(page)

        return render(request, 'notice_list.html', {
            'name': '公示公告',
            'lists': lists,
            'option': option,

        })


# 支队制度
class TeamSystemList(View):
    def get(self, request):
        # 进行选项
        option = request.GET.get('option', '')

        if option == '1' or option == '':
            lists = TeamSystem.objects.all().order_by('-add_time')
        else:
            lists = Submission.objects.all().order_by('-add_time')

        # 进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(lists, 1, request=request)

        lists = p.page(page)

        return render(request, 'team_system_list.html', {
            'name': '支队制度',
            'lists': lists,
            'option': option,

        })


# 法律法规
class LawsList(View):
    def get(self, request):
        # 进行选项
        option = request.GET.get('option', '')

        if option == '1' or option == '':
            lists = Laws.objects.all().order_by('-add_time')
        else:
            lists = Submission.objects.all().order_by('-add_time')

        # 进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(lists, 1, request=request)

        lists = p.page(page)

        return render(request, 'laws_list.html', {
            'name': '法律法规',
            'lists': lists,
            'option': option,

        })


# 通知通告文章详情页
class AnnouncementDetails(View):
    def get(self, request, detail_id):
        # 进行选项
        option = request.GET.get('option', '')

        if option == '1' or option == '':
            new_detail = Announcement.objects.get(id=int(detail_id))
        else:
            new_detail = Submission.objects.get(id=int(detail_id))

        return render(request, 'detail.html', {
            'new_detail': new_detail

        })


# 工作简报详情页
class WorkBulletinDetails(View):
    def get(self, request, detail_id):
        # 进行选项
        option = request.GET.get('option', '')

        if option == '1' or option == '':
            new_detail = WorkBulletin.objects.get(id=int(detail_id))
        else:
            new_detail = Submission.objects.get(id=int(detail_id))

        return render(request, 'detail.html', {
            'new_detail': new_detail

        })


# 公示公告详情页
class NoticeDetails(View):
    def get(self, request, detail_id):
        # 进行选项
        option = request.GET.get('option', '')

        if option == '1' or option == '':
            new_detail = Notice.objects.get(id=int(detail_id))
        else:
            new_detail = Submission.objects.get(id=int(detail_id))

        return render(request, 'detail.html', {
            'new_detail': new_detail

        })


# 支队制度
class TeamSystemDetails(View):
    def get(self, request, detail_id):
        # 进行选项
        option = request.GET.get('option', '')

        if option == '1' or option == '':
            new_detail = TeamSystem.objects.get(id=int(detail_id))
        else:
            new_detail = Submission.objects.get(id=int(detail_id))

        return render(request, 'detail.html', {
            'new_detail': new_detail
        })


# 法律法规详情页
class LawsDetails(View):
    def get(self, request, detail_id):
        # 进行选项
        option = request.GET.get('option', '')

        if option == '1' or option == '':
            new_detail = Laws.objects.get(id=int(detail_id))
        else:
            new_detail = Submission.objects.get(id=int(detail_id))

        return render(request, 'detail.html', {
            'new_detail': new_detail
        })


# 404全局页面配置
def page_not_found(request):
    response = render_to_response('404.html',{})
    response.status_code = 404
    return response


# 500全局页面配置
def page_error(request):
    response = render_to_response('500.html',{})
    response.status_code = 500
    return response
