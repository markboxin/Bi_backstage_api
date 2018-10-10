from functools import reduce
from django.shortcuts import render
from .models import LbBiSellComboAmountCount as IbCombo
from .models import LbBiInterfOrderUnit as IbOrder
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
import json
from django.core.paginator import Paginator, InvalidPage, EmptyPage
import datetime
from django.views.decorators.cache import cache_page


# Create your views here.
def combo(request):
    # 图像展示
    # combo_id = request.GET.get("combo_id")
    # print(combo_id)
    start = request.GET.get("start", "")
    end = request.GET.get("end", "")
    print(start)
    aQ = Q()
    if start or end is not '':
        start_date = start
        end_data = end
        print(start_date)
        aQ.add(Q(sell_date__range=(start_date, end_data)), Q.OR)
    else:
        now = datetime.datetime.now()
        end_data = now.strftime("%Y%m%d")
        print(end_data)
        start_date1 = now - datetime.timedelta(days=31)
        start_date = start_date1.strftime("%Y%m%d")
        print(start_date)
        aQ.add(Q(sell_date__range=(start_date, end_data)), Q.OR)
    all_orders = IbCombo.objects.filter(aQ).values('sell_date').distinct().order_by('sell_date')
    lists = list(all_orders)
    # print(lists)
    sell_date = []
    for i in range(len(lists)):
        sell_date.append(lists[i]['sell_date'])
    print(sell_date)

    # sell_date = ['20180820','20180821','20180822','20180823','20180824','20180825','20180826','20180827','20180828',
    #              '20180829','20180830','20180831','20180901','20180902','20180903','20180904,''20180905','20180906',
    #              '20180907','20180908','20180909','20180910','20180911','20180912','20180913','20180914','20180915',
    #              '20180916','20180917','20180918','20180919','20180920']
    # id
    alist = IbCombo.objects.values("combo_id").distinct()
    alist = list(alist)
    print(alist)
    alist2 = []
    for i in range(len(alist)):
        alist2.append(alist[i]['combo_id'])

    resultList = []
    for index1 in alist2:
        all_combo = IbCombo.objects.filter(sell_date__range=(sell_date[0], sell_date[-1]), combo_id=index1).order_by("sell_date")
        # print(all_combo)
        combo_id = index1
        combo_amount = []
        combo_count = []
        # sell_date = []
        combo_name = []
        for index2 in all_combo:
            # combo_id.append(index3.combo_id)
            combo_amount.append(index2.combo_amount)
            combo_count.append(index2.combo_count)
            # sell_date.append(index2.sell_date)
            combo_name.append(index2.combo_name)
        combo_name = list(set(combo_name))
        # print(combo_name)
        if len(combo_name) != 0:
            combo_name = combo_name[0]
        else:
            combo_name = []
        resultList += [{
            "combo_id": combo_id,
            "combo_name": combo_name,
            "combo_amount": combo_amount,
            "combo_count": combo_count,
            # "sell_date": sell_date
        }]
    return JsonResponse({"code": 200, "msg": "操作成功", "sell_date": sell_date, "data": resultList})
    # return HttpResponse(json.dumps(resultList))


# @cache_page(60 * 10)
def order(request):
    """订单"""
    order_code = request.GET.get("order_code")
    operater = request.GET.get("operater")
    combo_name = request.GET.get("combo_name")
    agent_name = request.GET.get("agent_name")
    order_status = request.GET.get("order_status")
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
    # status = {'order_code':'','operater':'','combo_name':'','agent_name':'','pay_method':''}
    print(order_code)
    each_page = 30
    if order_code or operater or combo_name or agent_name or order_status\
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
            aQ1.add(Q(operater__contains=operater), Q.OR)
            aQ2.add(Q(operater__contains=operater), Q.AND)
            list1.append(operater)

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
            if order_status == '0':
                order_status1 = "待园务确认"
                order_status2 = "待网络测试"
                aQ1.add(Q(order_status_detail=order_status1), Q.OR)
                aQ1.add(Q(order_status_detail=order_status2), Q.OR)
                aQ2.add(Q(order_status_detail=order_status1), Q.AND)
                aQ2.add(Q(order_status_detail=order_status2), Q.AND)
            elif order_status == '1':
                order_status = "部分发货"
            elif order_status == '3':
                order_status = "待网络测试"
            elif order_status == '4':
                order_status = "待园务确认"
            elif order_status == '2':
                order_status = "全部发货"
            else:
                order_status = ""
            if order_status != '0':
                aQ1.add(Q(order_status_detail=order_status), Q.OR)
                aQ2.add(Q(order_status_detail=order_status), Q.AND)
            list1.append(order_status)
        if is_garden_confirm is not None:
            if is_garden_confirm == '1':
                is_garden_confirm = "是"
            else:
                is_garden_confirm = "否"
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
            if out_time1 == out_time2:
                start_date = datetime.datetime.strptime(out_time1, "%Y-%m-%d")
                end_data = datetime.datetime.strptime(out_time2, "%Y-%m-%d") + datetime.timedelta(days=1)
            else:
                start_date = datetime.datetime.strptime(out_time1, "%Y-%m-%d")
                end_data = datetime.datetime.strptime(out_time2, "%Y-%m-%d")
            print(start_date)

            aQ1.add(Q(out_time__range=(start_date, end_data)), Q.OR)
            aQ2.add(Q(out_time__range=(start_date, end_data)), Q.AND)
            list1.append(out_time1)

        if order_create_time1 or order_create_time2 is not None:
            if order_create_time1 == order_create_time2:
                start_date = datetime.datetime.strptime(order_create_time1, "%Y-%m-%d")
                end_data = datetime.datetime.strptime(order_create_time2, "%Y-%m-%d") + datetime.timedelta(days=1)
            else:
                start_date = datetime.datetime.strptime(order_create_time1, "%Y-%m-%d")
                end_data = datetime.datetime.strptime(order_create_time2, "%Y-%m-%d")
            print(start_date)

            aQ1.add(Q(order_create_time__range=(start_date, end_data)), Q.OR)
            aQ2.add(Q(order_create_time__range=(start_date, end_data)), Q.AND)
            list1.append(order_create_time1)
        print(aQ1)
        print(list1)
        page = int(request.GET.get('page', '1'))
        if len(list1) == 1:
            all_orders = IbOrder.objects.filter(aQ1).order_by('-order_create_time')
            school_number = IbOrder.objects.filter(aQ1).values('school_id').distinct().count()
            class_number = IbOrder.objects.filter(aQ1).values('class_id').distinct().count()
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
            school_number = IbOrder.objects.filter(aQ2).values('school_id').distinct().count()
            class_number = IbOrder.objects.filter(aQ2).values('class_id').distinct().count()
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
        all_orders = IbOrder.objects.all().order_by('-order_create_time')
        school_number = IbOrder.objects.values('school_id').distinct().count()
        class_number = IbOrder.objects.values('class_id').distinct().count()
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
            "sales_num":index.sales_num,
            "order_code": index.order_code,
            "agent_id": index.agent_id,
            "agent_name": index.agent_name,
            "operater": index.operater,
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
            "pay_voucher": index.pay_voucher
        }]

    # 返回值
    # response = JsonResponse(resultList, safe=False)
    # response.status_code = 500  自定义响应码
    return JsonResponse({"code": 200, "msg": "操作成功", "total": p_num, "school_number": school_number, "class_number": class_number, "data": resultList})
