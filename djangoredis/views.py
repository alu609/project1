from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def dredis(request):
    #设置redis保存的session是字符串类型，保存在服务器
    request.session['name']='alu'
    request.session['age'] = '666'
    #取出设置的sessionid值
    print(request.session['name'])
    #删除session,指定key值
    # del request.session['name']
    #清除里面所有的键和值
    # request.session.clear()
    #清除整条session
    request.session.flush()
    return HttpResponse('django-redis数据库')