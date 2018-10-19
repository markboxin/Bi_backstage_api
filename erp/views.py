
from .models import LbBiErpExport as Lberp
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
import json
from django.core.paginator import Paginator, InvalidPage, EmptyPage
import datetime

# Create your views here.
def erp(request):
    """订单"""
    order_code = request.GET.get("order_code")
    operater = request.GET.get("operater")
    agent_linkman = request.GET.get('agent_linkman')
    combo_name = request.GET.get("combo_name")
    school_name = request.GET.get("school_name")
    order_create_time1 = request.GET.get("order_create_time1")
    order_create_time2 = request.GET.get("order_create_time2")

    each_page = 30
    if order_code or operater or combo_name or school_name or order_create_time1 or order_create_time2 or agent_linkman:
        aQ1 = Q()
        aQ2 = Q()
        list1 = []
        if order_code is not None:
            aQ1.add(Q(order_code=order_code), Q.OR)
            aQ2.add(Q(order_code=order_code), Q.AND)
            list1.append(order_code)
        if agent_linkman is not None:
            aQ1.add(Q(agent_linkman__contains=agent_linkman), Q.OR)
            aQ2.add(Q(agent_linkman__contains=agent_linkman), Q.AND)
            list1.append(agent_linkman)
        if operater is not None:
            aQ1.add(Q(operater_name__contains=operater), Q.OR)
            aQ2.add(Q(operater_name__contains=operater), Q.AND)
            list1.append(operater)
        if combo_name is not None:
            aQ1.add(Q(combo_name__contains=combo_name), Q.OR)
            aQ2.add(Q(combo_name__contains=combo_name), Q.AND)
            list1.append(combo_name)

        if school_name is not None:
            aQ1.add(Q(school_name__contains=school_name), Q.OR)
            aQ2.add(Q(school_name__contains=school_name), Q.AND)
            list1.append(school_name)

        if order_create_time1 or order_create_time2 is not None:

            start_date = datetime.datetime.strptime(order_create_time1, "%Y-%m-%d")
            end_data = datetime.datetime.strptime(order_create_time2, "%Y-%m-%d") + datetime.timedelta(days=1)

            print(start_date)

            aQ1.add(Q(order_create_time__range=(start_date, end_data)), Q.OR)
            aQ2.add(Q(order_create_time__range=(start_date, end_data)), Q.AND)
            list1.append(order_create_time1)
        print(aQ1)
        print(list1)
        page = int(request.GET.get('page', '1'))
        if len(list1) == 1:
            all_orders = Lberp.objects.filter(aQ1).order_by('-order_create_time')
            if page == -1:
                p_num = Lberp.objects.filter(aQ1).count()
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
            all_orders = Lberp.objects.filter(aQ2).order_by('-order_create_time')
            if page == -1:
                p_num = Lberp.objects.filter(aQ2).count()
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
            all_orders = Lberp.objects.all().order_by('-order_create_time')
        except Lberp.DoesNotExist:
            return HttpResponse(status=404)
        page = int(request.GET.get('page', '1'))
        if page == -1:
            p_num = Lberp.objects.count()
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
    resultList = []
    print(contacts)
    for index in contacts:
        resultList += [{
            "order_code": index.order_code,
            "subjection_project": index.subjection_project,
            "combo_name": index.combo_name,
            "class_number": index.class_num,
            "school_name": index.school_name,
            "operater": index.operater_name,
            "order_create_time": index.order_create_time,
            "order_status": index.order_status,
            "pay_price": index.pay_price,
            "network_check": index.network_check,
            'agent_linkman': index.agent_linkman,
            "school_address": index.school_address,
        }]

    # 返回值
    # response = JsonResponse(resultList, safe=False)
    # response.status_code = 500  自定义响应码
    return JsonResponse({"code": 200, "msg": "操作成功", "total": p_num, "data": resultList})