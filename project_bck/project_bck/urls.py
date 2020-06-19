"""project_bck URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from user_info import views
from device_info import views as dev_view
from data_hub import views as received_payloads

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.user_list.as_view()),
    path('devices/', dev_view.device_list.as_view()),
    path('payloads/', received_payloads.payload_list.as_view())
]
