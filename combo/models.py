# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class LbBiInterfOrderUnit(models.Model):
    school_id = models.IntegerField(blank=True, primary_key=True)
    school_name = models.CharField(max_length=255, blank=True, null=True)
    class_name = models.CharField(max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    combo_id = models.IntegerField(blank=True, null=True)
    combo_name = models.CharField(max_length=255, blank=True, null=True)
    sales_unit_id = models.IntegerField(blank=True, null=True)
    sales_unit_name = models.CharField(max_length=255, blank=True, null=True)
    unit_price = models.FloatField(max_length=100, blank=True, null=True)
    sales_num = models.IntegerField(blank=True, null=True)
    order_code = models.CharField(max_length=255, blank=True, null=True)
    agent_id = models.CharField(max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    agent_name = models.CharField(max_length=255, blank=True, null=True)
    operater = models.CharField(max_length=255, blank=True, null=True)
    order_create_time = models.CharField(max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    order_price = models.FloatField(max_length=100,blank=True, null=True)
    pay_type = models.CharField(max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    pay_price = models.FloatField(max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    pay_method = models.CharField(max_length=255, blank=True, null=True)
    order_status = models.CharField(max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    inner_auditing_name = models.CharField(max_length=255, blank=True, null=True)
    inner_auditing_time = models.CharField(max_length=255, blank=True, null=True)
    inner_auditing_status = models.CharField(max_length=255, blank=True, null=True)
    inner_auditing_remark = models.CharField(max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    finance_auditing_name = models.CharField(max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    finance_auditing_time = models.CharField(max_length=255, blank=True, null=True)
    finance_auditing_status = models.CharField(max_length=255, blank=True, null=True)
    finance_auditing_remark = models.CharField(max_length=255, blank=True, null=True)
    is_device = models.CharField(max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    device_follow_name = models.CharField(max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    is_nerwork = models.CharField(max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    network_follow_name = models.CharField(max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    network_install_fee = models.CharField(max_length=255, blank=True, null=True)
    is_garden_confirm = models.BooleanField(max_length=255, default=False)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    garden_oper = models.CharField(max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    garden_confirm_time = models.CharField(max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    send_goods_status = models.CharField(max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    send_goods_code = models.CharField(max_length=255, blank=True, null=True)
    logistics_no = models.CharField(max_length=255, blank=True, null=True)
    is_plan = models.CharField(max_length=255)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    plan_complete = models.CharField(max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    plan_uncomplete = models.CharField(max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    order_status_detail = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'lb_bi_interf_order_unit'


class LbBiSellComboAmount(models.Model):
    combo_name = models.CharField(max_length=100, blank=True, null=True)
    sell_department = models.CharField(max_length=100, blank=True, null=True)
    combo_amount = models.CharField(max_length=100, blank=True, null=True)
    sell_date = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lb_bi_sell_combo_amount'


class LbBiSellComboAmountCount(models.Model):
    combo_id = models.CharField(max_length=100, blank=True, primary_key=True)
    combo_name = models.CharField(max_length=200, blank=True, null=True)
    combo_amount = models.CharField(max_length=100, blank=True, null=True)
    combo_count = models.CharField(max_length=100, blank=True, null=True)
    sell_date = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lb_bi_sell_combo_amount_count'


class LbBiSellComboNum(models.Model):
    combo_name = models.CharField(max_length=100, blank=True, null=True)
    sell_department = models.CharField(max_length=100, blank=True, null=True)
    combo_count = models.CharField(max_length=100, blank=True, null=True)
    sell_date = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lb_bi_sell_combo_num'


class LbDemoLesson(models.Model):
    # id = models.IntegerField(blank=True, null=True)
    lesson_date = models.DateTimeField(blank=True, null=True)
    booking_date = models.DateTimeField(blank=True, null=True)
    kindergarten = models.CharField(max_length=255, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=255, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    teacher_name = models.CharField(max_length=255, blank=True, null=True)
    lesson_status = models.CharField(max_length=255, blank=True, null=True)
    customer = models.CharField(max_length=255, blank=True, null=True)
    operator = models.CharField(max_length=255, blank=True, null=True)
    cellphone = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lb_demo_lesson'



