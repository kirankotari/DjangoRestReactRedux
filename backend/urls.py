"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include
from rest_framework import routers
from django.contrib import admin
from django.urls import path
from backendapp import views as backendapp_views
from frontendapp import urls as frontendapp_urls



router = routers.DefaultRouter()


urlpatterns = [
	path('', include(frontendapp_urls)),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('rates', backendapp_views.RatesViewSet.as_view()),
]


