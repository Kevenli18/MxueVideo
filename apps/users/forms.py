#!_*_coding: utf-8 _*_
# @author =  lijun
# date  =  2018/6/26/026 17:14

from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5, widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    captcha = CaptchaField(required=True, error_messages={'invalid': '验证码错误！'}) #error_messages自定义错误信息


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(required=True, error_messages={'invalid': '验证码错误！'}) #error_messages自定义错误信息


class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)





