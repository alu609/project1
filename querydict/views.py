from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def query(request):
    print(request.GET.get('name'))
    print(request.GET.get('age'))
    return HttpResponse('查询响应体数据')