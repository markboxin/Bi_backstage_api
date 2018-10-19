from django.shortcuts import render

# Create your views here.

from .models import LbBiOrderFlow as LbOf
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
import json
from django.core.paginator import Paginator, InvalidPage, EmptyPage
import datetime


# Create your views here.
def orderflow(request):
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
            all_orders = LbOf.objects.filter(aQ1)
            if page == -1:
                p_num = LbOf.objects.filter(aQ1).count()
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
            all_orders = LbOf.objects.filter(aQ2)
            if page == -1:
                p_num = LbOf.objects.filter(aQ2).count()
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
            all_orders = LbOf.objects.all()
        except LbOf.DoesNotExist:
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
            "combo_name": index.combo_name,
            "class_number": index.class_number,
            "partial_delivery": index.partial_delivery,
            "pending_delivery": index.pending_delivery,
            "waiting_network_test": index.waiting_network_test,
            "waiting_garden_confirm": index.waiting_garden_confirm,
            "all_delivery": index.all_delivery,
            "order_complete": index.order_complete,
            "no_plan": index.no_plan,
            "is_plan": index.is_plan,
            "class_corrected_number": index.class_corrected_number,
            "arranged_formal_courses": index.arranged_formal_courses,
            "confirm_time": index.confirm_time,
        }]

    # 返回值
    # response = JsonResponse(resultList, safe=False)
    # response.status_code = 500  自定义响应码
    return JsonResponse({"code": 200, "msg": "操作成功", "total": p_num, "data": resultList})

