from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def object(request):
    print(request.POST.getlist('name'))
    print(request.POST.get('age'))
    return HttpResponse('获取post请求体数据')