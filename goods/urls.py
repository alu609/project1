from django.conf.urls import url,include

from . import views
#子路由寻找视图函数
urlpatterns = [
    #设置视图函数路径
    # url(r'^index', views.index)
    #设置视图函数的正确输入路径，只能在子应用添加
    url(r'^list/$', views.list,name='list')
]