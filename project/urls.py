"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
#由总路由寻找子路由方式
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #设置子路由路径
    url(r'^user/', include('user.urls')),
    url(r'^goods/', include('goods.urls')),
    url(r'^parameter/', include('parameter.urls')),
    url(r'^dcookie/',include('dcookie.urls')),
    url(r'^arguments/',include('arguments.urls')),
    url(r'^querydict/',include('querydict.urls')),
    url(r'^queryobject/',include('queryobject.urls')),
    url(r'^querybody/',include('querybody.urls')),
    url(r'^queryheader/',include('queryheader.urls')),
    url(r'^response/',include('response.urls')),
    url(r'^jsonresponse/',include('jsonresponse.urls')),

]
