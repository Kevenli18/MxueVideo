#!_*_coding: utf-8 _*_
# @author =  lijun
# date  =  2018/6/26/026 10:32

import xadmin

from .models import CityDirt, CourseOrg, Teacher


class CityDirtAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'add_time']
    search_fields = ['name', 'desc', 'click_nums']
    list_filter = ['name', 'desc', 'click_nums', 'add_time']


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company']
    search_fields = ['org', 'name', 'work_years', 'work_company']
    list_filter = ['org', 'name', 'work_years', 'work_company']


xadmin.site.register(CityDirt, CityDirtAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)




