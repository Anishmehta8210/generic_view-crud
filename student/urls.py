"""student URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from detail.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', TeacherView.as_view(),name="home"),
     path('insert/', TeacherFormView.as_view(),name="insert"),
     path('<pk>/delete-teacher', TeacherDeleteView.as_view(),name="TeacherDeleteView"),
     path('<pk>/edit-teacher', TeacherEditView.as_view(),name="TeacherEditView"),
     path('login/', LoginView.as_view(),name="LoginView"),
     path('logout/', LogoutView.as_view(),name="LogoutView"),
]
