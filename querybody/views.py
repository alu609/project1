import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def qubody(request):

    """
    print(request.body.decode())
    """

    #获取非form表单请求体数据
    print(request.body)
    #查看数据类型
    print(type(request.body))
    json_str = request.body
    # json_str = json_str.decode()
    #将json数据转化为字典
    str_data = json.loads(json_str)
    print(str_data)


    return HttpResponse("请求体使用body方式进行获取数据")