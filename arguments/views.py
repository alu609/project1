from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def argument(request,year,city):
    print(city)
    print(year)
    # print(request.GET.get[year])
    return HttpResponse('命名参数的获取')