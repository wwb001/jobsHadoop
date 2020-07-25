"""mysite URL Configuration
url 与 函数 的关系
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
from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse,render
from mysite.views import *
from mysite import settings

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/', login),
    path('login/TestServlet', TestServlet),
    path('getMapMessage', getMapMessage),
    path('getCityNum', getCityNum),
    path('getValue', getValue),
    path('getNeedNum', getNeedNum),
    path('getAvSala', getAvSala),
    path('getFiveAvSala', getFiveAvSala),
    path('getTotalMap',getTotalMap),
    path('getHotCity',getHotCity),
    path('getJobNum',getJobNum),
    path('getJobSalary',getJobSalary),
    path('domesticdemand',guoneixuqiu),
    path('totaldemand',gangweizongxuqiu),
    path('averagesalary',gangweipingjunxinzi),
    path('pro-averagesalary',shengpingjunxinzi),
    path('hotword',zhaopingaopinci),
    path('main',main),
    path('3dSalaryPart',dSalaryPart)
]
