#!_*_coding: utf-8 _*_
# @author =  lijun
# date  =  2018/6/30/030 9:19

from django.conf.urls import url, include


from .views import CourseListView, CourseDetailView
urlpatterns = [

    #课程列表页
    url(r'^list/$', CourseListView.as_view(), name='list'),
    # 课程详情页
    url(r'^detail/(?P<course_id>\d+)/', CourseDetailView.as_view(), name='detail'),
]
