from django.shortcuts import render
from django.views.generic.base import View

from .models import Duty
from custom.models import LogoImage

# Create your views here.


class IntroduceView(View):
    def get(self, request):
        # Logo
        logos = LogoImage.objects.all().order_by('-add_time')
        return render(request, 'introduce.html', {
            'name': '支队介绍',
            'logos': logos,
        })


class DutyView(View):
    def get(self, request):
        monday = []
        tuesday = []
        wednesday = []
        thursday = []
        friday = []
        saturday = []
        sunday = []
        try:
            monday = Duty.objects.filter(week=0).order_by('-add_time')[0]
            tuesday = Duty.objects.filter(week=1).order_by('-add_time')[0]
            wednesday = Duty.objects.filter(week=2).order_by('-add_time')[0]
            thursday = Duty.objects.filter(week=3).order_by('-add_time')[0]
            friday = Duty.objects.filter(week=4).order_by('-add_time')[0]
            saturday = Duty.objects.filter(week=5).order_by('-add_time')[0]
            sunday = Duty.objects.filter(week=6).order_by('-add_time')[0]
        except:
            pass

        week = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]

        return render(request, 'duty.html', {
            'name': '值班表',
            'Weeks': week,

        })
