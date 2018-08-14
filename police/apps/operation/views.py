from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
# 重定向
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from .forms import SubmissionAskForm
from .models import Submission


class SubmissionAsk(View):
    def get(self, request):
        return render(request, 'submission.html', {
        })

    def post(self, request):
        title = ''
        content = ''
        name = ''
        phone = ''
        address = ''
        email = ''
        error = ''

        submission_form = SubmissionAskForm(request.POST)
        if submission_form.is_valid():
            submission_form.save(commit=True)
            return redirect(reverse('operation:success', args=[]))
        else:
            title = request.POST.get('title', '')
            content = request.POST.get('content', '')
            name = request.POST.get('name', '')
            phone = request.POST.get('phone', '')
            address = request.POST.get('address', '')
            email = request.POST.get('email', '')
            error = submission_form.errors

        return render(request, 'submission.html', {
            'name': '用户投稿',
            'title': title,
            'content': content,
            'sub_name': name,
            'phone': phone,
            'address': address,
            'email': email,
            'error': error,
        })


class SuccessView(View):
    def get(self, request):
        return render(request, 'success.html', {
            'name': '投稿成功'
        })
