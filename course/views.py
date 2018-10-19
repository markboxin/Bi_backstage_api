
from .models import LbBiTeacherPlan as LbTeacher
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
import json
from django.core.paginator import Paginator, InvalidPage, EmptyPage
import datetime

# Create your views here.
def course(request):
    """课程"""
    course_datetime1 = request.GET.get("course_datetime1")
    course_datetime2 = request.GET.get("course_datetime2")
    # course_state = request.GET.get('course_state')
    each_page = 30
    if course_datetime1 or course_datetime2:
        aQ1 = Q()
        aQ2 = Q()
        list1 = []
        if course_datetime1 or course_datetime2 is not None:

            start_date = datetime.datetime.strptime(course_datetime1, "%Y-%m-%d")
            end_data = datetime.datetime.strptime(course_datetime2, "%Y-%m-%d") + datetime.timedelta(days=1)

            print(start_date)
            aQ1.add(Q(course_datetime__range=(start_date, end_data)), Q.OR)
            aQ2.add(Q(course_datetime__range=(start_date, end_data)), Q.AND)
            list1.append(course_datetime1)
        print(aQ1)
        print(list1)
        page = int(request.GET.get('page', '1'))
        if len(list1) == 1:
            all_orders = LbTeacher.objects.filter(aQ1).order_by('-course_datetime')
            if page == -1:
                p_num = LbTeacher.objects.filter(aQ1).count()
                print(p_num)
                contacts = all_orders
            else:
                paginator = Paginator(all_orders, each_page)
                p_num = paginator.count
                print(p_num)
                try:
                    contacts = paginator.page(page)
                    print(contacts)
                except(EmptyPage, InvalidPage):
                    contacts = paginator.page(paginator.num_pages)
        else:
            all_orders = LbTeacher.objects.filter(aQ2).order_by('-course_datetime')
            if page == -1:
                p_num = LbTeacher.objects.filter(aQ2).count()
                print(p_num)
                contacts = all_orders
            else:
                paginator = Paginator(all_orders, each_page)
                p_num = paginator.count
                print(p_num)
                try:
                    contacts = paginator.page(page)
                    print(contacts)
                except(EmptyPage, InvalidPage):
                    contacts = paginator.page(paginator.num_pages)
    else:
        try:
            all_orders = LbTeacher.objects.all().order_by('-course_datetime')
        except LbTeacher.DoesNotExist:
            return HttpResponse(status=404)
        page = int(request.GET.get('page', '1'))
        if page == -1:
            return JsonResponse({'code': 400, 'msg': '数据量太多，请输入查询时间'})
        else:
            paginator = Paginator(all_orders, each_page)
            p_num = paginator.count
            print(p_num)
            try:
                contacts = paginator.page(page)
                print(contacts)
            except(EmptyPage, InvalidPage):
                contacts = paginator.page(paginator.num_pages)
    resultList = []
    print(contacts)
    for index in contacts:
        resultList += [{
            "course_date": index.course_date,
            "course_time": index.course_time,
            "teacher_name": index.teacher_name,
            "course_type": index.course_type,
            "teacher_from": index.teacher_from,
            "course_datetime": index.course_datetime,
            "course_state": index.course_state,
        }]

    # 返回值
    # response = JsonResponse(resultList, safe=False)
    # response.status_code = 500  自定义响应码
    return JsonResponse({"code": 200, "msg": "操作成功", "total": p_num, "data": resultList})

