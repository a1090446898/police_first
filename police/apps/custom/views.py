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
        week = []
        try:
            all_monday = Duty.objects.filter(week=0).order_by('-add_time')
            all_tuesday = Duty.objects.filter(week=1).order_by('-add_time')
            all_wednesday = Duty.objects.filter(week=2).order_by('-add_time')
            all_thursday = Duty.objects.filter(week=3).order_by('-add_time')
            all_friday = Duty.objects.filter(week=4).order_by('-add_time')
            all_saturday = Duty.objects.filter(week=5).order_by('-add_time')
            all_sunday = Duty.objects.filter(week=6).order_by('-add_time')

        except:
            pass

        if all_monday:
            monday = all_monday[0]
        if all_tuesday:
            tuesday = all_tuesday[0]
        if all_wednesday:
            wednesday = all_wednesday[0]
        if all_thursday:
            thursday = all_thursday[0]
        if all_friday:
            friday = all_friday[0]
        if all_saturday:
            saturday = all_saturday[0]
        if all_sunday:
            sunday = all_sunday[0]
        week = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]

        return render(request, 'duty.html', {
            'name': '值班表',
            'weeks': week,

        })
