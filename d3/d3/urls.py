"""d3 URL Configuration

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
from d3 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('html1/', views.html1, name="html1"),
    path('html2/', views.html2, name="html2"),
    path('html3/', views.html3, name="html3"),
    path("urls_data/<name>",views.urls_data, name = "urls_data"),
    path("ab/<ab>",views.ab,name="ab"),
    path("grt/<grt>",views.grt, name ="grt"),
    path("vow/<s>", views.vow, name = "vow"),
    


]
