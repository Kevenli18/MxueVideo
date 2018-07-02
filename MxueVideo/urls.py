from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.static import serve

import xadmin
import captcha

from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetUserView, ModifyPwdView
from organization.views import OrgView
from MxueVideo.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='user_register'),  #(?P<active_code>.*)正则P是参数，
    url(r'^forgetpwd/', ForgetPwdView.as_view(), name='forget_pwd'),
    url(r'^reset/(?P<active_code>.*)/$', ResetUserView.as_view(), name='reset'),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name='modify'),

    #课程机构配置
    url(r'^org/', include('organization.urls', namespace='org')),

    #课程相关配置
    url(r'^course/', include('courses.urls', namespace='course')),

    #处理图片显示的url，使用Django自带server，传入参数告诉它去哪个路劲找
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),


]
