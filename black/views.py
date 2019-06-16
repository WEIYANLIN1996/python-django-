from django.shortcuts import render
from black.models import Posts
from black.models import Comment
from black.models import Information
from black.models import Img
from black.models import Answer
from django.http import JsonResponse
from django.core.paginator import Paginator , PageNotAnInteger,EmptyPage
# Create your views here.

def index(request):
    info = Information.objects.filter(receive_name=request.session['username'], read_sure=False)
    contact_list = Posts.objects.all().order_by("-create_time")
    paginator = Paginator(contact_list,7)  # Show 25 contacts per page

    page = request.GET.get('page','1')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request,'blackmain/index.html',{'contacts': contacts,'paginator':paginator})

def gooodclass(request):
    contact_list = Posts.objects.all().order_by("-create_time")
    paginator = Paginator(contact_list, 12)  # Show 25 contacts per page

    page = request.GET.get('page', '1')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    if len(contacts)>=4 and len(contacts)<8:
        list1=[contacts[0],contacts[1],contacts[2],contacts[3]]
    elif len(contacts)>=8 and len(contacts)<12:
        list1 = [contacts[0], contacts[1], contacts[2], contacts[3]]
        list2 = [contacts[4], contacts[5], contacts[6], contacts[7]]
    elif len(contacts)>=12:
        list1 = [contacts[0], contacts[1], contacts[2], contacts[3]]
        list2 = [contacts[4], contacts[5], contacts[6], contacts[7]]
        list3 = [contacts[8], contacts[9], contacts[10], contacts[11]]
    else:
        list1 = [contacts[0], contacts[1], contacts[2], contacts[3]]
    print(len(list1))
    return render(request, 'blackmain/goodclass.html', {'contacts': contacts, 'paginator': paginator,'list1':list1,'list2':list2,'list3':list3})


def bw(request):
    contact_list = Posts.objects.filter(source_type="百度网盘教程").order_by("-create_time")
    paginator = Paginator(contact_list, 7)  # Show 25 contacts per page

    page = request.GET.get('page', '1')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'blackmain/bw.html', {'contacts': contacts, 'paginator': paginator})

def bcym(request):
    contact_list = Posts.objects.filter(source_type="开源源码").order_by("-create_time")
    paginator = Paginator(contact_list, 7)  # Show 25 contacts per page

    page = request.GET.get('page', '1')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'blackmain/bcym.html', {'contacts': contacts, 'paginator': paginator})

def answer(request):
    answer_list=Answer.objects.all().order_by("-question_time")
    print (answer_list)
    return render(request,'blackmain/answer.html',{'answer':answer_list})


def getcoin(request):
    if request.method == "GET":
            zy_comment = Comment.objects.filter(source_id=111111)
            context = {
                'zy_comment': zy_comment,
            }
            print(zy_comment)
            return render(request, 'blackmain/getcoin.html', context)
    else:
        return JsonResponse({'res': "无此页面"})


def enjoy(request):
    return render(request,'blackmain/enjoy.html')

def vip(request):

    return render(request,'blackmain/vip.html')

def posts(request):
    if request.method=="POST":
        title = request.POST.get('title')
        content = request.POST.get('sourcedsp')
        source_bgurl = request.POST.get('source_bgurl')
        source_psw = request.POST.get('source_psw')
        source_valuemarks = request.POST.get('sourcevalue')
        source_type = request.POST.get('source_type')
        share_name = request.POST.get('share_name')
        try:
            passport = Posts(title=title,content=content,source_picurl="11",source_psw=source_psw,source_bgurl=source_bgurl,source_valuemarks=source_valuemarks,source_type=source_type,share_name=share_name)
            passport.save()
            new_img = Img(
                img=request.FILES.get('sourceimg'),
                wpurl=source_bgurl
            )
            new_img.save()

        except Exception as e:
            print("e: ", e)  # 把异常打印出来
        return render(request, 'blackmain/enjoy.html')
    else:
        return render(request,'users/user_center_info.html')


def comment(request):
    if request.method=="POST":
        comment_sourcename=request.POST.get('comment_sourcename')
        source_id = request.POST.get('source_id')
        source_name = request.POST.get('source_name')
        comment_content = request.POST.get('comment_content')
        comment_name = request.POST.get('comment_name')
        info_tx=comment_name+"评论你的:"+comment_sourcename+" 资源"+comment_content
        try:
            passport = Comment(comment_sourcename=comment_sourcename, source_id=source_id,comment_content=comment_content,comment_name=comment_name)
            passport.save()

            info = Information(info_content=info_tx,receive_name=comment_sourcename, send_name=comment_name)
            info.save()

        except Exception as e:
            print("e: ", e)  # 把异常打印出来
            return JsonResponse({'res': 1, 'errmsg': 'failed'})

        return JsonResponse({'res': 0, 'errmsg': 'success'})
    else:
        return JsonResponse({'res': 1, 'errmsg': 'failed'})

def question(request):
    if request.method=="POST":
        tw_name=request.POST.get("twname")
        twcontent=request.POST.get('twcontent')
        try:
            tw = Answer(question_name=tw_name, question_content=twcontent)
            tw.save()
        except Exception as e:
            print("e: ", e) # 把异常打印出来
            return JsonResponse({'res': 1, 'errmsg': '提交失败'})
        return JsonResponse({'res': 0, 'errmsg': '提交成功'})
    else:
        return JsonResponse({'res': 4, 'errmsg': '请求错误'})
