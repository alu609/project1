from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#创建视图函数
from django.urls import reverse


def index(request):
    url=reverse('goods:list')
    #返回内容
    return HttpResponse(url)


