from django.shortcuts import render
from user.models import Users
from black.models import Posts
from black.models import Buys
from black.models import Comment
from black.models import Information
from black.models import Answer
from django.http import JsonResponse
from django.core.paginator import Paginator , PageNotAnInteger,EmptyPage
# Create your views here.
def source(request):
    if request.method=="GET":
        sid = request.GET.get('n')
        if sid=="":
            return JsonResponse({'res': "无此页面"})
        else:
            source = Posts.objects.filter(id=sid)
            zy_comment=Comment.objects.filter(source_id=sid)
            buysource = Buys.objects.filter(source_id=sid)
            #source_img = Img.objects.filter(wpurl=source[0].source_bgurl)
            context={
                'title': source[0].title,
                'content': source[0].content,
                'source_bgurl': source[0].source_bgurl,
                'source_psw':source[0].source_psw,
                'source_valuemarks': source[0].source_valuemarks,
                'click_nums': source[0].click_nums,
                'load_nums': source[0].load_nums,
                'source_price': source[0].source_price,
                'share_name': source[0].share_name,
                'source_id': source[0].id,
                'share_time':source[0].create_time,
                'zy_comment':zy_comment,
                'buysource':buysource,
            }
            print(zy_comment)
            return render(request,'other/contentzy.html',context)
    else:
        return JsonResponse({'res': "无此页面"})

def send(send_name,content,receive_name):
    try:
        buy = Information(send_name=send_name, receive_name=receive_name, info_content=content)
        buy.save()
    except Exception as e:
        print("e: ", e)



def buy(request):
    if request.method=="POST":
        user_name = request.POST.get('user_name')
        source_id=request.POST.get('source_id')
        source_value=request.POST.get('source_value')
        source = Buys.objects.filter(id=source_id)

        for record in source:
            if record.user==user_name:
                return JsonResponse({'res': 1, 'errmsg': '您已购买此资源'})
            else:
                continue
        user = Users.objects.get(username=user_name)
        if int(user.user_allmarks)>=int(source_value):
            user_allmarks=int(user.user_allmarks)-int(source_value)
            user.user_allmarks=user_allmarks
            user.save()
        else:
            return JsonResponse({'res': 2, 'errmsg': '积分不足'})
        try:
            buy=Buys(source_id=source_id,user=user_name,source_value=source_value)
            buy.save()
        except Exception as e:
            print("e: ", e)
            return JsonResponse({'res': 3, 'errmsg': '购买失败'})

        posts = Posts.objects.get(id=source_id)
        posts.load_nums = posts.load_nums + 1
        posts.save()
        source = Posts.objects.filter(id=source_id)
        send_name="系统消息"
        content="你已兑换资源"+str(source[0].title)+"网盘/开源网址"+str(source[0].source_bgurl)+" 网盘密码："+str(source[0].source_psw)
        send(send_name,content,request.session['username'])
        return JsonResponse({'res': 0,'bgurl':source[0].source_bgurl,'psw':source[0].source_psw})
    else:
        return JsonResponse({'res': "无此页面"})


def seacher(request):
    if request.method=="GET":
        skey=request.GET.get('seacherkey')
        if not skey:
            error_msg = '请输入关键词'
            return render(request, 'other/seacher.html', {'error_msg': error_msg})
        else:
            contact_list = Posts.objects.filter(title__icontains=skey).order_by("-create_time")
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

            return render(request, 'other/seacher.html', {'contacts': contacts, 'paginator': paginator,'num':len(contact_list),'key':skey})
    else:
        return JsonResponse({'res': "无此页面"})
