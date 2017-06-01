"""Riis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from home.views import *
from portal.views import *

admin.site.site_header = 'Rental Information System Admin.'

urlpatterns = [

#   home urls 
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'home.views.index', name='home'),
    url(r'^faq/', 'home.views.contact', name='faq'),
    url(r'^about/', About.as_view(), name='about'),
    
#    poratl urls
    
    url(r'^portal/', Portal.as_view(), name='portal'),
    url(r'^house.data/', houses_view, name='houses'),
    url(r'^road.data/', roads_view, name='roads'),
    url(r'^boundary.data/', boundary_view, name='boundary'),
    url(r'^highway.data/', highway_view, name='highway'),
    url(r'^procareas.data/', procareas_view, name='proctareas'),

# Registration Urls
    url(r'^accounts/register/$', SignUpView.as_view(), name='signup'),
    url(r'^accounts/login/$', LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', LogOutView.as_view(), name='logout'),
]
