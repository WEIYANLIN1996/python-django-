from django.db import models

# Create your models here.
from django.utils import timezone

class Posts(models.Model):
    """
    资源帖子
    """
    title = models.CharField(verbose_name='标题', max_length=100)
    content = models.TextField(verbose_name='资源介绍', default='')
    source_picurl = models.CharField(max_length=100, verbose_name='资源图片展示地址')
    source_bgurl = models.CharField(verbose_name='资源网盘或开源连接', max_length=300)
    source_psw = models.CharField(verbose_name='资源网盘密码', max_length=150,default='')
    source_valuemarks = models.IntegerField(default=50, verbose_name='资源值B币数')
    source_type = models.CharField(verbose_name='资源类型',max_length=150)
    create_time = models.DateTimeField(verbose_name='分享时间', default=timezone.now)
    click_nums = models.IntegerField(verbose_name='浏览量', default=0)
    load_nums = models.IntegerField(verbose_name='使用量', default=0)
    share_name = models.CharField(verbose_name='分享资源用户名', max_length=100)
    source_price= models.IntegerField(verbose_name='市场价值', default=80)

    class Meta:
        db_table= 'Posts_list'
        verbose_name = '我的资源'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    评论表
    """
    comment_sourcename = models.CharField(verbose_name='评论资源用户名', max_length=100)
    comment_name = models.CharField(verbose_name='评论用户名', max_length=100)
    source_id = models.IntegerField(db_column='sourceid', default=1,verbose_name='评论资源id')
    comment_content= models.TextField(verbose_name='评论内容', default='？？')
    comment_time = models.DateTimeField(verbose_name='评论时间', default=timezone.now)
    class Meta:
        db_table= 'Comment_list'
        verbose_name = '评论表'
        verbose_name_plural = verbose_name



class Information(models.Model):
    """
    消息表
    """
    send_name = models.CharField(verbose_name='发消息用户名', max_length=100)
    receive_name = models.CharField(verbose_name='接收者用户名', max_length=100)
    info_content = models.TextField(verbose_name='消息内容', default='？？')
    send_time = models.DateTimeField(verbose_name='发送时间', default=timezone.now)
    read_sure=models.BooleanField(verbose_name='是否已经被阅读',default= False)

    class Meta:
        db_table= 'Info_list'
        verbose_name = '消息表'
        verbose_name_plural = verbose_name



class Buys(models.Model):
    '''已被使用资源表'''

    source_id = models.IntegerField(db_column='source_id',verbose_name='资源id')
    user = models.CharField(verbose_name='使用者用户名', max_length=100)
    use_time = models.DateTimeField(verbose_name='使用时间', default=timezone.now)
    source_value = models.IntegerField(verbose_name='资源价值', default=80)


    class Meta:
        db_table = 'buys_list'
        verbose_name = '已被使用资源'
        verbose_name_plural = verbose_name




class Img(models.Model):
    img = models.ImageField(upload_to='img',verbose_name="资源图片")
    img_name = models.CharField(max_length=20,verbose_name="图片名",default="1")
    wpurl=models.CharField(max_length=200,verbose_name="图片标识网盘地址")

    class Meta:
        db_table= 'Img_source'
        verbose_name = '资源图片'
        verbose_name_plural = verbose_name

class Answer(models.Model):

    question_name = models.CharField(verbose_name='提问者用户名', max_length=100)
    question_content = models.TextField(verbose_name='提问内容', default='？？')
    question_time = models.DateTimeField(verbose_name='提问时间', default=timezone.now)

    class Meta:
        db_table = 'question_list'
        verbose_name = '提问表'
        verbose_name_plural = verbose_name