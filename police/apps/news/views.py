from datetime import datetime
from django.shortcuts import render
from django.views.generic.base import View


from .models import *
from apps.work.models import *
from resources.models import Resources
from custom.models import LogoImage, MovieWindow, OtherConnections
from duty.models import Duty, DutyMan

# Create your views here.


# 计数方法
def nums(source):
    # work模型
    notice = source.notice_set.all().count()
    announcement = source.announcement_set.all().count()
    work_bulletin = source.workbulletin_set.all().count()
    team_system = source.teamsystem_set.all().count()
    laws = source.laws_set.all().count()
    work_list = [notice, announcement, work_bulletin, team_system, laws]
    work_sum = notice + announcement + work_bulletin + team_system + laws

    # news总数
    news = source.news_set.all().count()
    team = source.teamnews_set.all().count()
    place = source.placesnews_set.all().count()
    help_num = source.helpnews_set.all().count()
    video = source.videopatrol_set.all().count()
    build = source.buildwork_set.all().count()
    news_sum = news + team + place + help_num + video + build
    news_list = [news, team, place, help_num, video, build, news_sum]
    # 总数
    all_sum = work_sum + news_sum
    return all_sum


# 主页
class IndexView(View):
    def get(self, request):
        news_banner = News.objects.filter(is_banner=True)
        source_nums = {}
        sources = Source.objects.all()

        # 发帖排行
        for source in sources:
            source_nums[source] = nums(source)

        # 监管要闻
        news = News.objects.all().order_by('-add_time')[:6]
        title_new = news[0]
        # 支队动态
        team_news = TeamNews.objects.all().order_by('-add_time')[:6]
        # 各地动态
        places_news = PlacesNews.objects.all().order_by('-add_time')[:6]
        # 协助破案
        help_news = HelpNews.objects.all().order_by('-add_time')[:6]
        # 视频巡查
        video_natrols = VideoPatrol.objects.all().order_by('-add_time')[:6]
        # 党建工作
        build_works = BuildWork.objects.all().order_by('-add_time')[:6]
        # 公示公告
        notices = Notice.objects.all().order_by('-add_time')[:6]
        # 通知通告
        announcements = Announcement.objects.all().order_by('-add_time')[:6]
        # 工作简报
        work_bulletins = WorkBulletin.objects.all().order_by('-add_time')[:6]
        # 支队制度
        team_systems = TeamSystem.objects.all().order_by('-add_time')[:6]
        # 法律法规
        laws = Laws.objects.all().order_by('-add_time')[:6]
        # 专项工作
        special_works = SpecialWork.objects.all()
        # 资源下载
        resources = Resources.objects.all().order_by('-add_time')
        # Logo
        logos = LogoImage.objects.all().order_by('-add_time')
        if logos:
            logo = logos[0]
        else:
            logo = []
        # 飘窗
        windows = MovieWindow.objects.all().order_by('-add_time')
        if windows:
            window = windows[0]
        else:
            window = []
        # 值日0-6表示星期一到星期日
        now_time = datetime.now()
        week_now = datetime.now().weekday()
        try:
            duty = Duty.objects.get(week=week_now)
        except Duty.DoesNotExist:
            duty = []
        if duty:
            duty_man_ld = duty.dutyman_set.order_by('-add_time').filter(type='ld')[0]
            duty_man_mj = duty.dutyman_set.order_by('-add_time').filter(type='mj')[0]
        else:
            duty_man_ld = []
            duty_man_mj = []
        # 各所链接
        other_urls = OtherConnections.objects.all().order_by('-add_time')
        # if other_urls:
        #     other_urls = []

        return render(request, 'index_base.html', {
            'all_News_banner': news_banner,
            'all_News': news,
            'new_title_id': title_new.id,
            'title_new': title_new,
            'all_team_news': team_news,
            'all_places_news': places_news,
            'all_help_news': help_news,
            'all_video_natrols': video_natrols,
            'all_build_works': build_works,
            'all_notices': notices,
            'all_announcements': announcements,
            'all_work_bulletins': work_bulletins,
            'all_team_systems': team_systems,
            'all_laws': laws,
            'all_special_works': special_works,
            'all_resources': resources,
            'source_nums': source_nums,
            'logo': logo,
            'window': window,
            'duty_man_ld': duty_man_ld,
            'duty_man_mj': duty_man_mj,
            'time': now_time,
            'other_urls': other_urls

        })


# 新闻列表页
class NewsList(View):
    def get(self):
        pass


# 新闻详情页
class NewsDetail(View):
    def get(self, request, new_id):
        new_detail = News.objects.get(id=int(new_id))
        new_detail.read_volume += 1
        new_detail.save()
        return render(request, 'detail.html', {
            'new_detail': new_detail,

        })
