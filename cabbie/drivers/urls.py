from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.driver_list, name='list'),
]