from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    #服务端设置响应头信息
    # return HttpResponse(content="人生自古谁无死，留取丹心照汗青",status=404,content_type="txt",charset="gbk")
    #服务端设置响应头数据
    response = HttpResponse('我自横刀向天笑')
    #设置响应头状态码
    response.status_code=200
    #设置响应头其他属性
    response['username']='alu'
    #返回响应头
    return response