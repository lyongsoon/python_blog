from django.contrib import admin
from django.conf.urls import url
# from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index')

    url(r'^$', views.index, name='index'),
    # url(r'^$', views.detail, name='index'),
    # url(r'^$', views.about, name='index'),
]
