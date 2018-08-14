import re
from django import forms

from .models import *


class SubmissionAskForm(forms.ModelForm):

    class Meta:
        model = Submission
        fields = ['title', 'content', 'phone', 'email', 'name', 'address']

    def clean_content(self):
        '''
        对textarea数据进行处理
        '''
        content = self.cleaned_data['content']
        RE_CONTENT1 = r'\r\n'
        RE_CONTENT2 = r' '
        con1 = re.compile(RE_CONTENT1)
        con2 = re.compile(RE_CONTENT2)
        content = con1.sub('<br>',content)
        content = con2.sub('&nbsp',content)
        return content

    def clean_phone(self):
        '''
        验证手机号码是否合法
        '''
        phone = self.cleaned_data['phone']
        REGEX_PHONE = r'^1[358]\d{9}$|^147\d{8}$|^176\d{8}$'
        p = re.compile(REGEX_PHONE)
        if p.match(phone):
            return phone
        else:
            raise forms.ValidationError('手机号码非法', code='phone_invalid')

