#!_*_coding: utf-8 _*_
# @author =  lijun
# date  =  2018/6/28/028 11:57
import re

from django import forms
from operation.models import UserAsk


#这种Form遗弃
class LastUsersAskForm(forms.Form):
    name = forms.CharField(required=True, max_length=20, min_length=2)
    phone = forms.CharField(required=True, max_length=11, min_length=11)


class UserAskForm(forms.ModelForm):  #继承ModelForm的功能强大，可以直接提交到数据库中
    #my_filed = forms.CharField()    添加UserAsk没有的字段
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name'] #可选继承字段

    def clean_mobile(self):   #必须clean开头
        '''
        验证手机号码是否合法
        '''
        mobile = self.cleaned_data['mobile']   #自定义封装mobile
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|176\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError('手机号码非法', code='mobile_invalid')







