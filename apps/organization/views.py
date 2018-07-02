# _*_coding: utf-8 _*_
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.generic.base import View
from pure_pagination import Paginator, PageNotAnInteger
from django.http import HttpResponse

from operation.models import UserFavorite
from .models import CourseOrg, CityDirt
from .forms import UserAskForm

class OrgView(View):
    '''
    课程机构列表功能
    '''
    def get(self, request):
        all_orgs = CourseOrg.objects.all()
        add_city = CityDirt.objects.all()
        hot_orgs = all_orgs.order_by('-click_nums')[:3]
        #取出筛选城市
        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs =all_orgs.filter(city_id=int(city_id))

        #机构类别筛选
        cate_id = request.GET.get('ct', '')
        if cate_id:
            all_orgs = all_orgs.filter(category=cate_id)

        #排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                all_orgs = all_orgs.order_by('-students')
            elif sort == 'courses':
                all_orgs = all_orgs.order_by('-course_nums')
        orgs_onums = all_orgs.count()

        #对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs, 5, request=request)  #传入所有机构对象，每一页的数量
        orgs = p.page(page)

        return render(request, 'org-list.html', {
            'all_orgs': orgs,
            'all_city': add_city,
            'org_onums': orgs_onums,    #机构数量
            'city_id': city_id,         #城市
            'cate_id': cate_id,         #类别
            'hot_orgs': hot_orgs,       #授课机构排序
            'sort': sort,               #排序
        })


class AddUserAskForm(View):
    '''
    用户添加咨询
    '''
    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            user_ask = userask_form.save(commit=True)  #提交到数据库中,不需要实例化出来一个一个初始化
            return HttpResponse('{"status": "success"}', content_type='application/json')
        else:                                           #吃了很多次亏了，json数据，注意单双引号
            return HttpResponse('{"status":"fail", "msg":"添加出错"}', content_type='application/json')


class OrgHomeView(View):
    '''
    机构首页
    '''
    def get(self, request, org_id):
        current_page = 'home'
        #根据id找到课程机构
        course_org = CourseOrg.objects.get(id=int(org_id))
        #验证是否已收藏
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        #反向查询到课程机构的所有课程和老师
        all_courses = course_org.course_set.all()[0:4]
        all_teacher = course_org.teacher_set.all()[0:2]
        return render(request, 'org-detail-homepage.html', {
            'course_org': course_org,
            'all_courses': all_courses,
            'all_teacher': all_teacher,
            'current_page': current_page,
            'has_fav': has_fav
        })


class OrgCourseView(View):
    '''
    机构课程列表页
    '''
    def get(self, request, org_id):
        current_page = 'course'
        #根据id找到课程机构
        course_org = CourseOrg.objects.get(id=int(org_id))
        # 验证是否已收藏
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        #反向查询到课程机构的所有课程和老师
        all_courses = course_org.course_set.all()[0:4]
        return render(request, 'org-detail-course.html', {
            'course_org': course_org,
            'all_courses': all_courses,
            'current_page': current_page,
            'has_fav': has_fav,
        })


class OrgDescView(View):
    '''
    机构课程列表页
    '''
    def get(self, request, org_id):
        current_page = 'desc'
        #根据id找到课程机构
        course_org = CourseOrg.objects.get(id=int(org_id))
        # 验证是否已收藏
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        return render(request, 'org-detail-desc.html', {
            'course_org': course_org,
            'current_page': current_page,
            'has_fav': has_fav,
        })


class OrgTeacherView(View):
    '''
    机构教师页
    '''
    def get(self, request, org_id):
        current_page = 'teacher'
        #根据id找到课程机构
        course_org = CourseOrg.objects.get(id=int(org_id))
        # 验证是否已收藏
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        all_teacher = course_org.teacher_set.all()
        return render(request, 'org-detail-teachers.html', {
            'all_teacher': all_teacher,
            'course_org': course_org,
            'current_page': current_page,
            'has_fav': has_fav,
        })


class AddFavView(View):
    '''
    添加收藏，取消收藏
    '''
    def post(self, request):
        fav_id = request.POST.get('fav_id', 0)    #这边如果是空字符串，用int会报错
        fav_type = request.POST.get('fav_type', 0)

        if not request.user.is_authenticated():
            #判断用户登录状态
            return HttpResponse('{"status": "fail", "msg": "用户未登陆！"}', content_type='application/json')
        exist_records = UserFavorite.objects.filter(user=request.user, fav_id=int(fav_id), fav_type=int(fav_type))
        if exist_records:
            #如果记录已经存在，则表示用户取消收藏
            exist_records.delete()
            return HttpResponse('{"status": "success", "msg": "收藏！"}', content_type='application/json')
        else:
            user_fav = UserFavorite()
            if int(fav_id) > 0 and int(fav_type) > 0:
                user_fav.fav_id = int(fav_id)
                user_fav.user = request.user
                user_fav.fav_type = int(fav_type)
                user_fav.save()
                return HttpResponse('{"status": "success", "msg": "已收藏！"}', content_type='application/json')
            else:
                return HttpResponse('{"status": "fail", "msg": "收藏出错！"}', content_type='application/json')











