from django.shortcuts import render
from .models import LbBiInterfOrderUnitV1 as IbOrder
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
import json
from django.core.paginator import Paginator, InvalidPage, EmptyPage
import datetime
from django.views.decorators.cache import cache_page


# Create your views here.
def order(request):
    """订单"""
    order_code = request.GET.get("order_code")
    operater = request.GET.get("operater")
    combo_name = request.GET.get("combo_name")
    agent_name = request.GET.get("agent_name")
    order_status = request.GET.getlist("order_status[]")
    is_plan = request.GET.get("is_plan")
    school_name = request.GET.get("school_name")
    sales_unit_name = request.GET.get("sales_unit_name")
    is_garden_confirm = request.GET.get("s_garden_confirm") # 是否院务确认
    is_nerwork = request.GET.get("is_nerwork") # 网络测试是否通过
    # print(school_name)
    order_create_time1 = request.GET.get("order_create_time1")
    order_create_time2 = request.GET.get("order_create_time2")
    unpaid_amount = request.GET.get("unpaid_amount")
    school_address = request.GET.get("school_address")
    out_time1 = request.GET.get("out_time1")
    out_time2 = request.GET.get("out_time2")
    pay_voucher = request.GET.get("pay_voucher")
    agent_linkman = request.GET.get("agent_linkman")
    # status = {'order_code':'','operater':'','combo_name':'','agent_name':'','pay_method':''}
    # print(order_code)
    print('--------')
    print(order_status)
    each_page = 30
    if order_code or operater or combo_name or agent_name or order_status or agent_linkman\
            or is_plan or school_name or order_create_time1 or order_create_time2 or\
            sales_unit_name or is_garden_confirm or is_nerwork or unpaid_amount or school_address or out_time1 or pay_voucher:
        aQ1 = Q()
        aQ2 = Q()
        list1 = []
        if order_code is not None:
            aQ1.add(Q(order_code=order_code), Q.OR)
            aQ2.add(Q(order_code=order_code), Q.AND)
            list1.append(order_code)
        if operater is not None:
            aQ1.add(Q(operater_name__contains=operater), Q.OR)
            aQ2.add(Q(operater_name__contains=operater), Q.AND)
            list1.append(operater)
        if agent_linkman is not None:
            aQ1.add(Q(agent_linkman__contains=agent_linkman), Q.OR)
            aQ2.add(Q(agent_linkman__contains=agent_linkman), Q.AND)
            list1.append(agent_linkman)

        if unpaid_amount is not None:
            aQ1.add(Q(unpaid_amount=unpaid_amount), Q.OR)
            aQ2.add(Q(unpaid_amount=unpaid_amount), Q.AND)
            list1.append(unpaid_amount)
        if school_address is not None:
            aQ1.add(Q(school_address__contains=school_address), Q.OR)
            aQ2.add(Q(school_address__contains=school_address), Q.AND)
            list1.append(school_address)
        if pay_voucher is not None:
            aQ1.add(Q(pay_voucher=pay_voucher), Q.OR)
            aQ2.add(Q(pay_voucher=pay_voucher), Q.AND)
            list1.append(pay_voucher)

        if combo_name is not None:
            aQ1.add(Q(combo_name__contains=combo_name), Q.OR)
            aQ2.add(Q(combo_name__contains=combo_name), Q.AND)
            list1.append(combo_name)
        if agent_name is not None:
            aQ1.add(Q(agent_name__contains=agent_name), Q.OR)
            aQ2.add(Q(agent_name__contains=agent_name), Q.AND)
            list1.append(agent_name)

        if order_status is not None:
            if len(order_status) != 0:
                for i in range(len(order_status)):
                    aQ1.add(Q(order_status_detail=order_status[i]), Q.OR)
                    aQ2.add(Q(order_status_detail=order_status[i]), Q.OR)
            list1.append(order_status)

        if is_garden_confirm is not None:
            if is_garden_confirm == '0':
                is_garden_confirm = "已确认"
            elif is_garden_confirm == '1':
                is_garden_confirm = "待确认"
            elif is_garden_confirm == '2':
                is_garden_confirm = '延后处理'
            aQ1.add(Q(is_garden_confirm=is_garden_confirm), Q.OR)
            aQ2.add(Q(is_garden_confirm=is_garden_confirm), Q.AND)
            list1.append(is_garden_confirm)
        if is_nerwork is not None:
            if is_nerwork == '1':
                is_nerwork = "是"
            else:
                is_nerwork = "否"
            aQ1.add(Q(is_nerwork=is_nerwork), Q.OR)
            aQ2.add(Q(is_nerwork=is_nerwork), Q.AND)
            list1.append(is_nerwork)
        if is_plan is not None:
            if is_plan == '1':
                is_plan = "是"
            else:
                is_plan = "否"
            aQ1.add(Q(is_plan=is_plan), Q.OR)
            aQ2.add(Q(is_plan=is_plan), Q.AND)
            list1.append(is_plan)
        if school_name is not None:
            aQ1.add(Q(school_name__contains=school_name), Q.OR)
            aQ2.add(Q(school_name__contains=school_name), Q.AND)
            list1.append(school_name)
        if sales_unit_name is not None:
            aQ1.add(Q(sales_unit_name__contains=sales_unit_name), Q.OR)
            aQ2.add(Q(sales_unit_name__contains=sales_unit_name), Q.AND)
            list1.append(sales_unit_name)
        if out_time1 or out_time2 is not None:

            start_date = datetime.datetime.strptime(out_time1, "%Y-%m-%d")
            end_data = datetime.datetime.strptime(out_time2, "%Y-%m-%d") + datetime.timedelta(days=1)

            aQ1.add(Q(out_time__range=(start_date, end_data)), Q.OR)
            aQ2.add(Q(out_time__range=(start_date, end_data)), Q.AND)
            list1.append(out_time1)

        if order_create_time1 or order_create_time2 is not None:

            start_date = datetime.datetime.strptime(order_create_time1, "%Y-%m-%d")
            end_data = datetime.datetime.strptime(order_create_time2, "%Y-%m-%d") + datetime.timedelta(days=1)

            aQ1.add(Q(order_create_time__range=(start_date, end_data)), Q.OR)
            aQ2.add(Q(order_create_time__range=(start_date, end_data)), Q.AND)
            list1.append(order_create_time1)
        print(aQ1)
        print(list1)
        page = int(request.GET.get('page', '1'))
        if len(list1) == 1:
            all_orders = IbOrder.objects.filter(aQ1).order_by('-order_create_time')
            school_number = IbOrder.objects.filter(aQ1).filter(school_id__isnull=False).values('school_id').distinct().count()
            class_number = IbOrder.objects.filter(aQ1).filter(class_id__isnull=False).values('class_id').distinct().count()
            if page == -1:
                p_num = IbOrder.objects.filter(aQ1).count()
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
            all_orders = IbOrder.objects.filter(aQ2).order_by('-order_create_time')
            school_number = IbOrder.objects.filter(aQ2).filter(school_id__isnull=False).values('school_id').distinct().count()
            class_number = IbOrder.objects.filter(aQ2).filter(class_id__isnull=False).values('class_id').distinct().count()
            if page == -1:
                p_num = IbOrder.objects.filter(aQ2).count()
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
        all_orders = IbOrder.objects.all().order_by('-order_create_time')
        school_number = IbOrder.objects.filter(school_id__isnull=False).values('school_id').distinct().count()
        class_number = IbOrder.objects.filter(class_id__isnull=False).values('class_id').distinct().count()
        print(school_number)
        print(class_number)
        page = int(request.GET.get('page', '1'))
        if page == -1:
            p_num = IbOrder.objects.count()
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
            "school_id": index.school_id,
            "school_name": index.school_name,
            "class_name": index.class_name,
            "class_id": index.class_id,
            "combo_id": index.combo_id,
            "combo_name": index.combo_name,
            "sales_unit_id": index.sales_unit_id,
            "sales_unit_name": index.sales_unit_name,
            "unit_price": index.unit_price,
            "sales_num": index.sales_num,
            "order_code": index.order_code,
            "agent_id": index.agent_id,
            "agent_name": index.agent_name,
            "operater": index.operater_name,
            "order_create_time": index.order_create_time,
            "order_price": index.order_price,
            "pay_type": index.pay_type,
            "pay_price": index.pay_price,
            "pay_method": index.pay_method,
            "order_status": index.order_status_detail,
            "inner_auditing_name": index.inner_auditing_name,
            "inner_auditing_time": index.inner_auditing_time,
            "inner_auditing_status": index.inner_auditing_status,
            "inner_auditing_remark": index.inner_auditing_remark,
            "finance_auditing_name": index.finance_auditing_name,
            "finance_auditing_time": index.finance_auditing_time,
            "finance_auditing_status": index.finance_auditing_status,
            "finance_auditing_remark": index.finance_auditing_remark,
            "is_device": index.is_device,
            "device_follow_name": index.device_follow_name,
            "is_nerwork": index.is_nerwork,
            "network_follow_name": index.network_follow_name,
            "network_install_fee": index.network_install_fee,
            "is_garden_confirm": index.is_garden_confirm,
            "garden_oper": index.garden_oper,
            "garden_confirm_time": index.garden_confirm_time,
            "send_goods_status": index.send_goods_status,
            "send_goods_code": index.send_goods_code,
            "logistics_no": index.logistics_no,
            "is_plan": index.is_plan,
            "plan_complete": index.plan_complete,
            "plan_uncomplete": index.plan_uncomplete,
            "unpaid_amount": index.unpaid_amount,
            "school_address": index.school_address,
            "out_time": index.out_time,
            "pay_voucher": index.pay_voucher,
            "operater_id": index.operater_id,
            "stock_out_num": index.stock_out_num,
            "agent_linkman": index.agent_linkman,
            "subjection_project": index.subjection_project
        }]

    # 返回值
    # response = JsonResponse(resultList, safe=False)
    # response.status_code = 500  自定义响应码
    return JsonResponse({"code": 200, "msg": "操作成功", "total": p_num, "school_number": school_number, "class_number": class_number, "data": resultList})