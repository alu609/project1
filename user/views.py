from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

#创建视图函数
from django.urls import reverse

def index(request):


    #返回内容
    return redirect(reverse('goods:list'))


