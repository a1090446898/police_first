import re
from django import forms

from .models import *


class EmailAskForm(forms.ModelForm):

    class Meta:
        model = Submission
        fields = ['name', 'title', 'content', 'phone', 'address', 'email']

    def clean_phone(self):
        '''
        验证手机号码是否合法
        '''
        phone = self.cleaned_data['phone']
        REGEX_PHONE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        p = re.compile(REGEX_PHONE)
        if p.match(REGEX_PHONE):
            return phone
        else:
            raise forms.ValidationError('手机号码非法', code='phone_invalid')
