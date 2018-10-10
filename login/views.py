from django.contrib.auth.models import User
# Create your views here.
import json
from .models import UserInfo
from django.http import HttpResponse, JsonResponse
from django import forms
from django.views.generic import View


def acc_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(request.POST)
        print("Pusername：" + username)
        print("password：" + password)
        try:
            user = UserInfo.objects.filter(username=username, password=password).first()
        except UserInfo.DoesNotExist:
            return HttpResponse(status=404)

            # print("passed authencation", user)
            # login(request, user)  # 登录可以显示用户
            # request.user = user
            # request.session['username'] = username
            # request.session.set_expiry(60 * 60 * 12 * 2)
        if user.is_staff == 1:
            return JsonResponse({"code": 200, "username": username})

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


class UserListView(View):
    """
    查询所有用户信息，增加用户
    """
    def get(self, request):
        """
        查询所有用户
        路由：GET/userlist/
        :param request:
        :return:
        """
        name = request.GET.get('username', '')
        if name:
            queryset = UserInfo.objects.filter(username__contains=name)
        else:
            queryset = UserInfo.objects.all()
        user_list = []
        for user in queryset:
            user_list.append({
                'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'is_staff': user.is_staff
            })
        return JsonResponse(user_list, safe=False)

    def post(self, request):
        """
        新增用户
        路由：POST/userlist/
        :param request:
        :return:
        """
        json_bytes = request.body
        json_str = json_bytes.decode()
        user_dict = json.loads(json_str)

        username = user_dict['username']
        username2 = UserInfo.objects.filter(username=username)
        if username2:
            return JsonResponse({"code": 400, "msg": "用户名已有"})
        user = UserInfo.objects.create(
            username=user_dict.get('username'),
            first_name=user_dict.get('first_name'),
            password=user_dict.get('password'),
            is_staff=True
        )

        return JsonResponse({
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'is_staff': user.is_staff
        })


class UserDetailView(View):

    def put(self, request, pk):
        try:
            user = UserInfo.objects.get(id=pk)
        except UserInfo.DoesNotExist:
            return HttpResponse(status=404)

        json_bytes = request.body
        json_str = json_bytes.decode()
        user_dict = json.loads(json_str)

        user.username = user_dict.get('username')
        user.password = user_dict.get('password')
        user.first_name = user_dict.get('first_name')
        user.save()

        return JsonResponse({
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'is_staff': user.is_staff
        })

    def delete(self, request, pk):
        try:
            user = UserInfo.objects.get(id=pk)
        except UserInfo.DoesNotExist:
            return HttpResponse(status=404)

        json_bytes = request.body
        json_str = json_bytes.decode()
        user_dict = json.loads(json_str)

        is_staff = user_dict.get('is_staff')
        if is_staff == 1:
            user.is_staff = 0
            user.save()
        else:
            user.is_staff = 1
            user.save()

        return JsonResponse({
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'is_staff': user.is_staff
        })

# def user_list(request):
#     # 用户列表
#     name = request.GET.get("username", "")
#     if name:
#         print(name)
#         all_users = UserInfo.objects.filter(username__contains=name)
#     else:
#         all_users = UserInfo.objects.all()
#     resultList = []
#     for index in all_users:
#         resultList += [{
#             "username": index.username,
#             "first_name": index.first_name,
#         }]
#     # 返回值
#     # response = JsonResponse(resultList, safe=False)
#     # response.status_code = 500  自定义响应码
#     return HttpResponse(json.dumps(resultList), content_type='application/json')
#
#
# class UserForm(forms.Form):
#     username = forms.CharField(label='用户名', max_length=100)
#     first_name = forms.CharField(label='姓名')
#     password = forms.CharField(label='密码')
#     # is_staff = forms.BooleanField(label='是否在职')
#
#
# def regist(request):
#     print(request.POST)
#     print(request.method)
#     print(request.body)
#     if request.method == 'POST':
#         uf = UserForm(request.POST)  # 包含用户名和姓名
#         if uf.is_valid():
#             username = uf.cleaned_data['username']  # cleaned_data类型是字典，里面是提交成功后的信息
#             user_name = UserInfo.objects.filter(username=username)
#             print(username)
#             if user_name:
#                 return JsonResponse({"code": 400, "msg": "用户名已有"})
#             first_name = uf.cleaned_data['first_name']
#             password = uf.cleaned_data["password"]
#             print("Pusername" + username)
#             # password = '111111'
#             # 添加到数据库
#             # registAdd = User.objects.get_or_create(username=username,password=password)
#             registAdd = UserInfo.objects.create(username=username, first_name=first_name, password=password)
#             # print registAdd
#             if registAdd:
#                 return JsonResponse({"code": 200})
#             else:
#                 # return HttpResponse('ok')
#                 return JsonResponse({"code": 401})
#     else:
#         return JsonResponse({"code": 402, "msg": "get请求返回页面"})


