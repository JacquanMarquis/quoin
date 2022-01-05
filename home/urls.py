from django.contrib import admin
from django.urls import path, include
from home import views

# Django admin header customization
admin.site.site_title = "Quoin's Dashboard"
admin.site.site_header = "Login to Bit Quoin"
admin.site.index_title = "Welcome to Bit Quoin"

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('projects', views.project, name='projects'),

    #path('project', views.dashboard, name='dashboard'),
    #path('project', views.vendorHome, name='vendorHome'),
    #path('project', views.vendorContact, name='vendorContact'),
]