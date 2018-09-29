from django.contrib.auth.models import User
# Create your views here.
import json

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import login
from django import forms
from .models import UserInfo

def acc_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(request.POST)
        print("Pusername：" + username)
        print("password：" + password)
        user = UserInfo.objects.filter(username=username, password=password).first()
        # 用户去做验证
        if user:
            # print("passed authencation", user)
            # login(request, user)  # 登录可以显示用户
            # request.user = user
            return JsonResponse({"code": 200, "username": username})

        else:
            return JsonResponse({"code": 401})
    else:
        return HttpResponse('get请求返回login.html')


# @login_required
def acc_logout(request):
    # 退出
    auth.logout(request)
    return JsonResponse({"code":200})


# 首页
def index(request):
    return HttpResponse('ok')


def user_list(request):
    # 用户列表
    name = request.GET.get("username", "")
    if name:
        print(name)
        all_users = User.objects.filter(username__contains=name)
    else:
        all_users = User.objects.all()
    resultList = []
    for index in all_users:
        resultList += [{
            "username": index.username,
            "first_name": index.first_name,
        }]
    # 返回值
    # response = JsonResponse(resultList, safe=False)
    # response.status_code = 500  自定义响应码
    return HttpResponse(json.dumps(resultList), content_type='application/json')


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    first_name = forms.CharField(label='姓名')
    # is_staff = forms.BooleanField(label='是否在职')


def regist(request):
    print(request.POST)
    print(request.method)
    print(request.body)
    if request.method == 'POST':
        uf = UserForm(request.POST)  # 包含用户名和姓名
        if uf.is_valid():
            username = uf.cleaned_data['username']  # cleaned_data类型是字典，里面是提交成功后的信息
            user_name = User.objects.filter(username=username)
            print(username)
            if user_name:
                return JsonResponse({"code": 400, "msg": "用户名已有"})
            first_name = uf.cleaned_data['first_name']
            print("Pusername" + username)
            password = '111111'
            # 添加到数据库
            # registAdd = User.objects.get_or_create(username=username,password=password)
            registAdd = User.objects.create_user(username=username, first_name=first_name, password=password)
            # print registAdd
            if registAdd:
                return JsonResponse({"code": 200})
            else:
                # return HttpResponse('ok')
                return JsonResponse({"code": 401})
                # return render_to_response('share.html',{'registAdd':registAdd},context_instance = RequestContext(request))
    else:
        return JsonResponse({"code":402,"msg":"get请求返回页面"})


