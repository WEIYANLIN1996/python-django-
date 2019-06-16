# Generated by Django 2.1.1 on 2019-04-01 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(db_column='userid', default=1000)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, verbose_name='用户邮箱')),
            ],
        ),
    ]