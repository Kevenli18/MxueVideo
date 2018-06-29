#_*_coding: utf-8 _*_
# @author = lijun
# date  =  2018/6/26/026 9:40

import xadmin
from xadmin import views

from .models import EmailVerifyRecord, UserProfile, Banner  #继承的user，自动注册了


class BaseSetting(object):
    enable_themes = True   #主题
    use_bootswatch = True    #主题


class GlobalSettings(object):
    site_title = 'M视频教育后台管理'  #头部名称
    site_footer = 'M互联科技'  #地址名称
    menu_style = 'accordion'    #可折叠


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time'] #显示一列的内容
    search_fields = ['code', 'email', 'send_type']  #时间做搜索不好
    list_filter = ['code', 'email', 'send_type', 'send_time']  #筛选， 添加过滤器


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']  # 显示一列的内容
    search_fields = ['title', 'image', 'url', 'index']  # 时间做搜索不好
    list_filter = ['title', 'image', 'url', 'index', 'add_time']  # 筛选， 添加过滤器


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)


