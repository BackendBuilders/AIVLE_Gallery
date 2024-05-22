"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

from Gallery import views

app_name = 'gallery'

urlpatterns = [
    path('', views.gallery_list, name='index'),
    path('<int:picture_id>/', views.detail, name='detail'),
    path('comment/create/<int:picture_id>/', views.create_comment, name='create_comment'),
    path('<int:picture_id>/update/', views.update_post, name='update'),
    path('new_register/', views.new_register, name='new_register'),
    path('create/', views.create, name='create'),
    path('search/', views.search, name='search'),
]