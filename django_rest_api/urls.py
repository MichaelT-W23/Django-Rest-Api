"""
URL configuration for django_rest_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from notes_app.routes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home_page'),
    path('test_db_connection/', views.test_db_connection, name='test_connection'),
    path('get_users/', views.get_all_users, name='get_all_users'),
    path('users/register/', views.register_user, name='register_user'),
    path('users/login/', views.login_user, name='login_user'),
    path('notes/users/<int:user_id>/notes/', views.get_notes_by_user, name='get_notes_by_user'),
    path('notes/tag/<str:tag_name>/', views.get_notes_by_tag, name='get_notes_by_tag'),
    path('notes/users/<int:user_id>/tag/', views.get_all_tags, name='get_all_tags'),
    path('users/<str:username>/', views.get_user_by_username, name='get_user_by_username'),
]
