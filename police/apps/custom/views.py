from django.shortcuts import render
from django.views.generic.base import View

from .models import Duty

# Create your views here.


class IntroduceView(View):
    def get(self, request):

        return render(request, 'introduce.html', {
            'name': '支队介绍',

        })


class DutyView(View):
    def get(self, request):
        Monday = []
        Tuesday = []
        Wednesday = []
        Thursday = []
        Friday = []
        Saturday = []
        Sunday = []

        try:
            Monday = Duty.objects.filter(week=0).order_by('-add_time')[0]
            Tuesday = Duty.objects.filter(week=1).order_by('-add_time')[0]
            Wednesday = Duty.objects.filter(week=2).order_by('-add_time')[0]
            Thursday = Duty.objects.filter(week=3).order_by('-add_time')[0]
            Friday = Duty.objects.filter(week=4).order_by('-add_time')[0]
            Saturday = Duty.objects.filter(week=5).order_by('-add_time')[0]
            Sunday = Duty.objects.filter(week=6).order_by('-add_time')[0]
        except:
            pass

        Week = [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]

        return render(request, 'duty.html', {
            'name': '值班表',
            'Weeks': Week,

        })
