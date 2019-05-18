from django.conf.urls import url

from querybody import views

urlpatterns = [
url(r'^qubody/$', views.qubody)
    ]