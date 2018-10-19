from django.contrib.auth.models import User
# Create your views here.
import json
from rbac.models import UserInfo
from django.http import HttpResponse, JsonResponse
from django import forms
from rbac.service.init_permission import init_permission
from django.views.generic import View
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password
from rbac.forms import UserInfoModelForm
from django.core import serializers


def acc_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(request.POST)
        print("Pusername：" + username)
        print("password：" + password)
        try:
            user = UserInfo.objects.filter(username=username, password=password).first()
            # if check_password(password, user.password):
            #     print('密码正确')
            # else:
            #     return HttpResponse('密码错误！'
        except UserInfo.DoesNotExist:
            return HttpResponse(status=404)

            # print("passed authencation", user)
            # login(request, user)  # 登录可以显示用户
            # request.user = user
            # request.session['username'] = username
            # request.session.set_expiry(60 * 60 * 12 * 2)
        if user.is_staff == 1:
            init_permission(request, user)

            menu = request.session[settings.SESSION_MENU_KEY]
            all_menu = menu[settings.ALL_MENU_KEY]
            permission_url = menu[settings.PERMISSION_MENU_KEY]
            # 定制数据结构
            all_menu_dict = {}
            for item in all_menu:
                item['isShow'] = True
                item['children'] = []
                all_menu_dict[item['id']] = item

            # request_rul = '/stock/in'
            import re

            for url in permission_url:
                # 添加两个状态：显示 和 展开
                url['isShow'] = True
                pattern = url['url']
                # if re.match(pattern, request_rul):
                #     url['open'] = True
                # else:
                #     url['open'] = False

                # 将url添加到菜单下
                all_menu_dict[url['menu_id']]["children"].append(url)
                # print('all_menu_Dict ---------------\n', all_menu_dict)
                # 显示菜单：url 的菜单及上层菜单 status: true
                pid = url['menu_id']
                while pid:
                    all_menu_dict[pid]['isShow'] = True
                    pid = all_menu_dict[pid]['parent_id']

                # 展开url上层菜单：url['open'] = True, 其菜单及其父菜单open = True
                # if url['open']:
                #     ppid = url['menu_id']
                #     while ppid:
                #         all_menu_dict[ppid]['open'] = True
                #         ppid = all_menu_dict[ppid]['parent_id']

            # 整理菜单层级结构：没有parent_id 的为根菜单， 并将有parent_id 的菜单项加入其父项的chidren内
            final_menu = []
            for i in all_menu_dict:
                # if all_menu_dict[i]['parent_id']:
                #     pid = all_menu_dict[i]['parent_id']
                #     parent_menu = all_menu_dict[pid]
                #     parent_menu['children'].append(all_menu_dict[i])
                # else:
                if all_menu_dict[i]['children']:
                    final_menu.append(all_menu_dict[i])

            print('final_menu ---------------\n', final_menu)

            return JsonResponse({"code": 200, "username": username, "final_menu": final_menu})

        else:
            return JsonResponse({"code": 401})
    else:
        return HttpResponse('get请求返回login.html')
        

# @login_required
def acc_logout(request):
    # 退出
    # auth.logout(request)
    # del request.session['username']
    return JsonResponse({"code": 200})


# 首页
def index(request):
    return HttpResponse('ok')


def userlist(request):

    if request.method == "GET":
        aQ = Q()
        name = request.GET.get('username', '')
        is_staff = request.GET.get('is_staff', '')
        if name or is_staff:
            if name:
                aQ.add(Q(username__contains=name), Q.OR)
            if is_staff:
                aQ.add(Q(is_staff=is_staff), Q.OR)
            queryset = UserInfo.objects.filter(aQ)
        else:
            queryset = UserInfo.objects.all()
        user_list = []
        print(queryset)
        for user in queryset:
            # user1 = UserInfo(username=user)
            # print(user1)
            # print(list(user.roles.all())[0])
            role = user.roles.all()
            role_json = serializers.serialize('json', role)
            roles_str = json.loads(role_json)
            roles = roles_str[0]['fields']['title']
            user_list.append({
                'id': user.id,
                'roles': roles,
                'username': user.username,
                'first_name': user.first_name,
                'is_staff': user.is_staff
            })
        return JsonResponse({'user_list': user_list, 'code': 200})
    else:
        pk = request.POST.get("pk")
        is_staff = request.POST.get('is_staff', '')
        print(is_staff)

        if pk:
            user_obj = UserInfo.objects.filter(id=pk).first()
            """修改"""
            if is_staff is not '':
                if is_staff == '0':
                    user_obj.is_staff = 0
                    user_obj.save()
                else:
                    user_obj.is_staff = 1
                    user_obj.save()
                return JsonResponse({'code': 200})
            else:
                model_form = UserInfoModelForm(request.POST, instance=user_obj)
                if model_form.is_valid():
                    model_form.save()
                    return JsonResponse({'code': 200})
                else:
                    return JsonResponse({'code': 401})

        else:
            # password = request.POST.get('password')
            # p = request.POST.copy()
            # npassword = make_password()
            # p.update({'password': npassword})
            # model_form = UserInfoModelForm(p)
            model_form = UserInfoModelForm(request.POST)
            # username = request.POST.get('username')
            # password = request.POST.get('password')
            # first_name = request.POST.get('first_name')
            # roles = request.POST.get('roles')
            # c = UserInfo(username=username,password=password,first_name=first_name,is_staff=True)
            # c.save()
            # c.roles.set(roles)
            # c.save()
            # return JsonResponse({'code': 200})
            # print(model_form)
            if model_form.is_valid():
                model_form.save()
                return JsonResponse({
                    'code': 200,
                })
            else:
                return JsonResponse({
                    'code': 401
                })


