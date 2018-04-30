"""Exalted URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import reverse_lazy
from .views.charm import *
from .filters import CharmFilter
from . import views

app_name='Exalted'

urlpatterns = [
    re_path(r'^charm/$', views.CharmIndexView.as_view(), name="charms"),
    re_path(r'^character/$', views.CharmIndexView.as_view(), name="characters"),
    re_path(r'^artifacts/$', views.CharmIndexView.as_view(), name="artifacts"),
    re_path(r'^other/$', views.CharmIndexView.as_view(), name="other"),
    path('charm/add/', CharmCreate.as_view(), name='charm-add'),
    path('charm/<int:pk>/', CharmUpdate.as_view(), name='charm-update'),
    path('charm/<int:pk>/delete/', CharmDelete.as_view(), name='charm-delete'),
    re_path(r'^charm/page/(?P<page>\d+)/$', views.CharmIndexView.as_view(), name='page'),

    path('admin/', admin.site.urls),
]

