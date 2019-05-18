from django.conf.urls import url

from queryheader import views

urlpatterns = [
url(r'^quheader/$', views.quheader)
    ]