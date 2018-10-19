# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class LbBiErpExport(models.Model):
    order_code = models.CharField(max_length=255, primary_key=True)
    subjection_project = models.CharField(max_length=50, blank=True, null=True)
    combo_name = models.CharField(max_length=255, blank=True, null=True)
    class_num = models.CharField(max_length=255, blank=True, null=True)
    school_name = models.CharField(max_length=255, blank=True, null=True)
    operater_name = models.CharField(max_length=255, blank=True, null=True)
    order_create_time = models.CharField(max_length=255, blank=True, null=True)
    order_status = models.CharField(max_length=255, blank=True, null=True)
    pay_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    network_check = models.CharField(max_length=255, blank=True, null=True)
    agent_linkman = models.CharField(max_length=255, blank=True, null=True)
    school_address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_lb_bi_erp_export'

