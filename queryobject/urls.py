from django.conf.urls import url

from queryobject import views

urlpatterns = [
url(r'^object/$', views.object)
    ]