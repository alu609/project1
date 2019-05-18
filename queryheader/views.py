from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def quheader(request):
    #获取全部请求头数据
    print(request.META)
    #获取请求头的数据类型
    print(request.META['CONTENT_TYPE'])
    #获取主机信息
    print(request.META['HTTP_HOST'])
    return HttpResponse("获取请求头数据")