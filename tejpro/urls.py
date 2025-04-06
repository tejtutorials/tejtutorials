"""
URL configuration for tejpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index1, name='index1'),
    # path('faculty', views.fac, name='fac'),
    path('faculty', views.fac1, name='fac1s'),
    # path('courses', views.cour, name='cour'),
    path('courses', views.cour1, name='cour1'),
    # path('whyus', views.whyus, name='whyus'),
    # path('connect', views.conwu, name='conwu'),
    path('connect', views.connect1, name='connect1'),
    # path('gallery', views.gal, name='gal'),
    path('gallery', views.gal1, name='gal1'),
    # path('index1', views.index1, name='index1'),
]
