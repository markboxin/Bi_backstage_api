from django.db import models

# Create your models here.


class UserInfo(models.Model):
    """
    用户表:
        1   张三        zhangsan    123   在职    角色
        2   lisi        123
        3   baolin      123
    """
    username = models.CharField(verbose_name="用户名", max_length=32, unique=True)
    password = models.CharField(verbose_name="密码", max_length=64)
    first_name = models.CharField(verbose_name="姓名", max_length=32)
    is_staff = models.BooleanField(verbose_name="是否在职", default=True)