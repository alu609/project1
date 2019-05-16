from django.conf.urls import url,include

from user import views
#子路由寻找视图函数
urlpatterns = [
    #设置视图函数路径
    url(r'^index/', views.index)
]

