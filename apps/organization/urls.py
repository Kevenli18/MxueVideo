#!_*_coding: utf-8 _*_
# @author =  lijun
# date  =  2018/6/28/028 14:30
from django.conf.urls import url, include

from organization.views import OrgView, AddUserAskForm, OrgHomeView

urlpatterns = [

    #课程机构首页列表
    url(r'^list/$', OrgView.as_view(), name='list'),
    url(r'^add_ask/$', AddUserAskForm.as_view(), name='add_ask'),
    url(r'^home/(?P<org_id>\d+)/', OrgHomeView.as_view(), name='org_home'),
]













