from django.conf.urls import url, include
from prestapi import views


urlpatterns = [
    url(r'^$', views.show_form, name='show_form'),
    ]