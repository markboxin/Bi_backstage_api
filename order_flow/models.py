# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class LbBiOrderFlow(models.Model):
    combo_name = models.CharField(max_length=255, primary_key=True)
    class_number = models.CharField(max_length=50, blank=True, null=True)
    partial_delivery = models.CharField(max_length=255, blank=True, null=True)
    pending_delivery = models.CharField(max_length=255, blank=True, null=True)
    waiting_network_test = models.CharField(max_length=255, blank=True, null=True)
    waiting_garden_confirm = models.CharField(max_length=255, blank=True, null=True)
    all_delivery = models.CharField(max_length=255, blank=True, null=True)
    order_complete = models.CharField(max_length=255, blank=True, null=True)
    no_plan = models.CharField(max_length=255, blank=True, null=True)
    is_plan = models.CharField(max_length=255, blank=True, null=True)
    class_corrected_number = models.CharField(max_length=255, blank=True, null=True)
    arranged_formal_courses = models.CharField(max_length=255, blank=True, null=True)
    confirm_time = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lb_bi_order_flow'











