"""blog URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#새로운 방식
from django.contrib import admin
from django.urls import include, path
# from django.conf.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feed/', include('feed.urls')),
]

# # 기존 방식
# from django.contrib import admin
# from django.conf.urls import include, url
# # from feed import views.py
#
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     # url(r'^', include('feed.urls')),
#     url(r'^$', views.index),
#     # url(r'^/', include.feed.urls),
# ]
