from django.conf.urls import url

from arguments import views

urlpatterns = [
url(r'^argument/(?P<year>\d{4})/(?P<city>[a-z]+)/', views.argument)
    ]