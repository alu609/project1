from django.conf.urls import url

from dcookie import views

urlpatterns = [
url(r'^recookie/$', views.recookie)
    ]