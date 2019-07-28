"""testing_house URL Configuration

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
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('login', views.login, name='login'),
    path('', views.index, name='index'),
    path('index', views.index, name='index'),

    path('user_list', views.user_list, name='user_list'),
    path('user_add', views.user_add, name='user_add'),
    path('user_data', views.user_data, name='user_data'),
    path('user_del', views.user_del, name='user_del'),
    path('user_locking', views.user_locking, name='user_locking'),
    path('user_reset_password', views.user_reset_password, name='user_reset_password'),
    url(r'^user_edit/name=(.*)', views.user_edit),
    url(r'^user_del_more', views.user_del_more),

    path('menu_add', views.menu_add, name='menu_add'),
    url(r'^menu_edit/menu_name=(.*)', views.menu_edit),
    path('menu_del', views.menu_del, name='menu_del'),
    path('menu_list', views.menu_list, name='menu_list'),
    path('menu_data', views.menu_data, name='menu_data'),

    path('form_list', views.form_list, name='form_list'),
    path('department_add', views.department_add, name='department_add'),
    path('department_list', views.department_list, name='department_list'),
    url(r'^department_edit/name=(.*)', views.department_edit),
    url(r'^department_set/name=(.*)', views.department_set),
    path('department_del', views.department_del, name='department_del'),
    path('department_data', views.department_data, name='department_data'),

    path('role_list', views.role_list, name='role_list'),
    path('role_data', views.role_data, name='role_data'),
    path('role_add', views.role_add, name='role_add'),
    path('role_del', views.role_del, name='role_del'),
    url(r'^role_edit/name=(.*)', views.role_edit),
    url(r'^role_user/name=(.*)', views.role_user),
    url(r'^role_del_more', views.role_del_more),

    path('group_list', views.group_list, name='group_list'),
    path('group_data', views.group_data, name='group_data'),
    path('group_add', views.group_add, name='group_add'),
    path('group_del', views.group_del, name='group_del'),
    url(r'^group_edit/name=(.*)', views.group_edit),
    url(r'^group_del_more', views.group_del_more),

    path('jobs_list', views.jobs_list, name='jobs_list'),
    path('jobs_data', views.jobs_data, name='jobs_data'),
    path('jobs_add', views.jobs_add, name='jobs_add'),
    path('jobs_del', views.jobs_del, name='jobs_del'),
    url(r'^jobs_edit/name=(.*)', views.jobs_edit),
    url(r'^jobs_del_more', views.jobs_del_more),

    path('password', views.password, name='password'),
    path('user_info', views.user_info, name='user_info'),
    path('user_form', views.user_form, name='user_form'),
    path('register', views.register, name='register'),
    path('forget', views.forget, name='forget'),
    path('logout', views.logout, name='logout'),
    path('set_email', views.set_email, name='set_email'),
    path('set_web', views.set_web, name='set_web'),
]
