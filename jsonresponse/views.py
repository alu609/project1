from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
def response(request):
    #创建json数据
    # json = {
    #     "a":1,
    #     "b":2,
    #     "c":3
    # }
    # return JsonResponse(json)
    #创建json列表数据
    # json1 = [{"a": 1,"b": 2},{"c": 3}]
    # return JsonResponse(json1,safe=False)

    #redirect重定向
    return redirect('/static/index.html')