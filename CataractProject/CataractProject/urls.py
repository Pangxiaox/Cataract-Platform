"""CataractProject URL Configuration

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
from django.conf.urls import url
from InformTable import views

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^postdiagnose/', views.postdiagnose),
    url(r'^patientslist/', views.showpatientlist),
    url(r'^editdiagnose/(?P<id>[0-9]*)/edit$', views.editdiagnose, name="edit"),
    url(r'^doctorlogin/', views.doctorlogin),
    url(r'^diagnose/(?P<id>[0-9]*)/delete$', views.deletediagnose, name="delete"),
    url(r'^doctorsignup/', views.doctorsignup),
    url(r'^doctorlogout/', views.doctorlogout)
]
