# Generated by Django 2.1.1 on 2019-04-15 14:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190401_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(db_column='userid', default=1000)),
                ('username', models.CharField(max_length=20, verbose_name='用户名')),
                ('password', models.CharField(max_length=40, verbose_name='用户密码')),
                ('description', models.CharField(max_length=200, verbose_name='个人说明')),
                ('email', models.EmailField(max_length=254, verbose_name='用户邮箱')),
                ('User_headpicurl', models.CharField(max_length=100, verbose_name='用户头像地址')),
                ('user_allmarks', models.IntegerField(db_column='user_mark', default=20, verbose_name='用户B币数')),
                ('register_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='注册时间')),
            ],
            options={
                'verbose_name': '所有用户',
                'verbose_name_plural': '所有用户',
                'db_table': 'Users_list',
            },
        ),
        migrations.AlterField(
            model_name='ulist',
            name='description',
            field=models.CharField(max_length=200, verbose_name='个人说明'),
        ),
        migrations.AlterField(
            model_name='ulist',
            name='password',
            field=models.CharField(max_length=40, verbose_name='用户密码'),
        ),
        migrations.AlterField(
            model_name='ulist',
            name='username',
            field=models.CharField(max_length=20, verbose_name='用户名'),
        ),
    ]