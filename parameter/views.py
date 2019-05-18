from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def sp(request,year,city):
    print(year)
    print(type(year))
    print(city)
    print(type(city))

    return HttpResponse("未命名参数按顺序传递")