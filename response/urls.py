from django.conf.urls import url

from response import views

urlpatterns = [
url(r'^login/$', views.login)
    ]