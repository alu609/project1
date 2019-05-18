from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def recookie(request):
    #设置响应体数据
    response = HttpResponse('cookie设置')
    #设置cookie值
    response.set_cookie('name','alu')
    #获取cookie值
    #获取cookie时，必须先进行cookie设置，然后才能获取到值
    print(request.COOKIES['name'])
    return response
