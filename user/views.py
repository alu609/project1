from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#创建视图函数
def index(request):
    #返回内容
    return HttpResponse('django,你好')


