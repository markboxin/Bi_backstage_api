# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class LbBiTeacherPlan(models.Model):
    course_date = models.CharField(primary_key=True, max_length=255)
    course_time = models.CharField(max_length=50, blank=True, null=True)
    teacher_name = models.CharField(max_length=255, blank=True, null=True)
    course_type = models.CharField(max_length=255, blank=True, null=True)
    teacher_from = models.CharField(max_length=255, blank=True, null=True)
    course_datetime = models.CharField(max_length=255, blank=True, null=True)
    course_state = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lb_bi_teacher_plan'


