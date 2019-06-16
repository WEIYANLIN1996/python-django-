from django.db import models
from django.utils import timezone
# Create your models here.

class Ulist(models.Model):
    userid = models.IntegerField(db_column='userid', default=1000)
    username = models.CharField(max_length=20,verbose_name='用户名')
    password = models.CharField(max_length=40,verbose_name='用户密码')
    description = models.CharField(max_length=200,verbose_name='个人说明')
    email = models.EmailField(verbose_name='用户邮箱')


class Users(models.Model):
    userid = models.IntegerField(db_column='userid', default=1000)
    username = models.CharField(max_length=20,verbose_name='用户名')
    password = models.CharField(max_length=40,verbose_name='用户密码')
    description = models.CharField(max_length=200,verbose_name='个人说明',default="")
    email = models.EmailField(verbose_name='用户邮箱')
    User_headpicurl=models.CharField(max_length=100, verbose_name='用户头像地址',default="")
    user_allmarks=models.IntegerField(db_column='user_mark', default=20,verbose_name='用户B币数')
    register_time=models.DateTimeField(verbose_name='注册时间', default=timezone.now)

    class Meta:
        db_table= 'Users_list'
        verbose_name = '所有用户'
        verbose_name_plural = verbose_name



