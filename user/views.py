from django.shortcuts import render
from django.http import JsonResponse
from user.models import Users
from black.models import Posts
from black.models import Information
from django.core.paginator import Paginator , PageNotAnInteger,EmptyPage
import re
from django.shortcuts import render, redirect, reverse




# Create your views here.
def login(request):
    if request.method=="GET":
        return render(request,'users/login.html',{'errmsg': ''})

    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('pwd')

        userlist = Users.objects.all()
        for var in userlist:
             if var.username==username and var.password==password:
                 request.session['islogin'] = True
                 request.session['username'] = username
                 request.session['user_id'] = var.userid
                 return JsonResponse({'res': 0, 'jump_url': 'http:127.0.0.1:8080/'})
             else:
                 continue
        return JsonResponse({'res': 1, 'errmsg': '登录失败'})

def logout(request):
    request.session['islogin'] = False
    del request.session['username']
    del request.session['user_id']
    # 跳转到首页
    return render(request,'users/login.html')

def resgister(request):
    if request.method=="GET":
        return render(request,'users/register.html', {'errmsg': ''})

    if request.method=="POST":
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        cpassword = request.POST.get('cpwd')
        email = request.POST.get('email')
        if not all([username, password, email]):
            # 有数据为空
            return render(request, 'users/register.html', {'errmsg': '参数不能为空!'})

        if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            # 邮箱不合法
            return render(request, 'users/register.html', {'errmsg': '邮箱不合法!'})
        if password!=cpassword:
            return render(request, 'users/register.html', {'errmsg': '两次密码不一致!'})
        try:
            new_data = Users.objects.order_by('-id')[:1]
            if len(new_data)>=1:
                newuid=new_data[0].userid+1
                passport = Users(username=username, password=password, email=email,userid=newuid)
            else:
                passport = Users(username=username, password=password, email=email)
            passport.save()
        except Exception as e:
            print("e: ", e)  # 把异常打印出来
            return render(request, 'users/register.html', {'errmsg': '用户名已存在！'})
        return render(request, 'users/login.html')

def user_center(request):
    user_info = Users.objects.get(username=request.session['username'])
    source = Posts.objects.filter(share_name=request.session['username'])
    info = Information.objects.filter(receive_name=request.session['username'],read_sure=False)
    paginator = Paginator(source,5)  # Show 25 contacts per page

    page = request.GET.get('page','1')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    context = {
        'zynum':len(source),
        'info_num':len(info),
        'contacts': contacts,
        'paginator': paginator,
        'user_info':user_info,
    }
    return render(request, 'users/user_center_info.html',context)

def user_forget(request):
    return render(request, 'users/user_center_order.html')

def payvip(request):
    return render(request, 'users/payvip.html')

def user_info(request):
    if request.method=="GET":
        user_info = Users.objects.get(username=request.session['username'])
        source = Posts.objects.filter(share_name=request.session['username'])
        info = Information.objects.filter(receive_name=request.session['username']).order_by('-send_time')
        info_n = Information.objects.filter(receive_name=request.session['username'], read_sure=False)
        context = {
            'zynum': len(source),
            'info':info,
            'info_num':len(info_n),
            'user_info': user_info,
        }
        return render(request, 'users/user_info.html', context)
    else:
        return JsonResponse({'res': 1, 'errmsg': '无效请求'})

def uinfo_modify(request):
    if request.method=="POST":
        username=request.POST.get('username')
        des=request.POST.get('des')
        user_info=Users.objects.get(username=request.session['username'])
        user_info.username=username
        user_info.description =des
        user_info.save()
        request.session['username'] = username
        return JsonResponse({'res':0,'errmsg': 'success'})

    else:
        return JsonResponse({'res': 1, 'errmsg': '无效请求'})