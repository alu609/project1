from django.conf.urls import url

from querydict import views

urlpatterns = [
url(r'^query/$', views.query)
    ]