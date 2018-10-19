# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class LbBiInterfOrderUnit(models.Model):
    school_id = models.CharField(max_length=255, primary_key=True)
    school_name = models.CharField(max_length=255, blank=True, null=True)
    class_name = models.CharField(max_length=255, blank=True, null=True)
    combo_id = models.CharField(max_length=255, blank=True, null=True)
    combo_name = models.CharField(max_length=255, blank=True, null=True)
    sales_unit_id = models.CharField(max_length=255, blank=True, null=True)
    sales_unit_name = models.CharField(max_length=255, blank=True, null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sales_num = models.IntegerField(blank=True, null=True)
    order_code = models.CharField(max_length=255, blank=True, null=True)
    agent_id = models.CharField(max_length=255, blank=True, null=True)
    agent_name = models.CharField(max_length=255, blank=True, null=True)
    operater = models.CharField(max_length=255, blank=True, null=True)
    order_create_time = models.CharField(max_length=255, blank=True, null=True)
    order_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pay_type = models.CharField(max_length=255, blank=True, null=True)
    pay_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pay_method = models.CharField(max_length=255, blank=True, null=True)
    order_status = models.CharField(max_length=255, blank=True, null=True)
    inner_auditing_name = models.CharField(max_length=255, blank=True, null=True)
    inner_auditing_time = models.CharField(max_length=255, blank=True, null=True)
    inner_auditing_status = models.CharField(max_length=255, blank=True, null=True)
    inner_auditing_remark = models.CharField(max_length=255, blank=True, null=True)
    finance_auditing_name = models.CharField(max_length=255, blank=True, null=True)
    finance_auditing_time = models.CharField(max_length=255, blank=True, null=True)
    finance_auditing_status = models.CharField(max_length=255, blank=True, null=True)
    finance_auditing_remark = models.CharField(max_length=255, blank=True, null=True)
    is_device = models.CharField(max_length=255, blank=True, null=True)
    device_follow_name = models.TextField(blank=True, null=True)
    is_nerwork = models.CharField(max_length=255, blank=True, null=True)
    network_follow_name = models.TextField(blank=True, null=True)
    network_install_fee = models.CharField(max_length=255, blank=True, null=True)
    is_garden_confirm = models.CharField(max_length=255, blank=True, null=True)
    garden_oper = models.CharField(max_length=255, blank=True, null=True)
    garden_confirm_time = models.CharField(max_length=255, blank=True, null=True)
    send_goods_status = models.CharField(max_length=255, blank=True, null=True)
    send_goods_code = models.CharField(max_length=255, blank=True, null=True)
    logistics_no = models.CharField(max_length=255, blank=True, null=True)
    is_plan = models.CharField(max_length=255, blank=True, null=True)
    plan_complete = models.TextField(blank=True, null=True)
    plan_uncomplete = models.TextField(blank=True, null=True)
    order_status_detail = models.CharField(max_length=255, blank=True, null=True)
    class_id = models.CharField(max_length=255, blank=True, null=True)
    unpaid_amount = models.CharField(max_length=255, blank=True, null=True)
    school_address = models.CharField(max_length=255, blank=True, null=True)
    out_time = models.CharField(max_length=255, blank=True, null=True)
    pay_voucher = models.CharField(max_length=255, blank=True, null=True)
    subjection_project = models.CharField(max_length=50, blank=True, null=True)
    agent_linkman = models.CharField(max_length=50, blank=True, null=True)
    stock_out_num = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lb_bi_interf_order_unit'


class LbBiInterfOrderUnitV1(models.Model):
    school_id = models.CharField(max_length=255, primary_key=True)
    school_name = models.CharField(max_length=255, blank=True, null=True)
    class_name = models.CharField(max_length=255, blank=True, null=True)
    combo_id = models.CharField(max_length=255, blank=True, null=True)
    combo_name = models.CharField(max_length=255, blank=True, null=True)
    sales_unit_id = models.CharField(max_length=255, blank=True, null=True)
    sales_unit_name = models.CharField(max_length=255, blank=True, null=True)
    unit_price = models.CharField(max_length=255, blank=True, null=True)
    sales_num = models.CharField(max_length=255, blank=True, null=True)
    order_code = models.CharField(max_length=255, blank=True, null=True)
    agent_id = models.CharField(max_length=255, blank=True, null=True)
    agent_name = models.CharField(max_length=255, blank=True, null=True)
    operater_id = models.CharField(max_length=255, blank=True, null=True)
    order_create_time = models.CharField(max_length=255, blank=True, null=True)
    order_price = models.CharField(max_length=255, blank=True, null=True)
    pay_type = models.CharField(max_length=255, blank=True, null=True)
    pay_price = models.CharField(max_length=255, blank=True, null=True)
    pay_method = models.CharField(max_length=255, blank=True, null=True)
    order_status = models.CharField(max_length=255, blank=True, null=True)
    inner_auditing_name = models.CharField(max_length=255, blank=True, null=True)
    inner_auditing_time = models.CharField(max_length=255, blank=True, null=True)
    inner_auditing_status = models.CharField(max_length=255, blank=True, null=True)
    inner_auditing_remark = models.CharField(max_length=255, blank=True, null=True)
    finance_auditing_name = models.CharField(max_length=255, blank=True, null=True)
    finance_auditing_time = models.CharField(max_length=255, blank=True, null=True)
    finance_auditing_status = models.CharField(max_length=255, blank=True, null=True)
    finance_auditing_remark = models.CharField(max_length=255, blank=True, null=True)
    is_device = models.CharField(max_length=255, blank=True, null=True)
    device_follow_name = models.TextField(blank=True, null=True)
    is_nerwork = models.CharField(max_length=255, blank=True, null=True)
    network_follow_name = models.TextField(blank=True, null=True)
    network_install_fee = models.CharField(max_length=255, blank=True, null=True)
    is_garden_confirm = models.CharField(max_length=255, blank=True, null=True)
    garden_oper = models.CharField(max_length=255, blank=True, null=True)
    garden_confirm_time = models.CharField(max_length=255, blank=True, null=True)
    send_goods_status = models.CharField(max_length=255, blank=True, null=True)
    send_goods_code = models.CharField(max_length=255, blank=True, null=True)
    logistics_no = models.CharField(max_length=255, blank=True, null=True)
    is_plan = models.CharField(max_length=255, blank=True, null=True)
    plan_complete = models.CharField(max_length=255, blank=True, null=True)
    plan_uncomplete = models.CharField(max_length=255, blank=True, null=True)
    order_status_detail = models.CharField(max_length=255, blank=True, null=True)
    class_id = models.CharField(max_length=255, blank=True, null=True)
    school_address = models.CharField(max_length=255, blank=True, null=True)
    pay_voucher = models.CharField(max_length=255, blank=True, null=True)
    out_time = models.CharField(max_length=255, blank=True, null=True)
    unpaid_amount = models.CharField(max_length=255, blank=True, null=True)
    stock_out_num = models.CharField(max_length=255, blank=True, null=True)
    agent_linkman = models.CharField(max_length=255, blank=True, null=True)
    subjection_project = models.CharField(max_length=255, blank=True, null=True)
    operater_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lb_bi_interf_order_unit_v1'




