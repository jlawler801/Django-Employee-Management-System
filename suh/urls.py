from re import template
from xml.etree.ElementInclude import include
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.scroop, name="home"),
    path('kroo/', views.kroo_view, name='kroo'),
    path('game/', views.employee_data, name='game'),
    path('role/', views.role_view, name='role'),
    path('beep/<int:id>/', views.emp_info_view, name='beep'),
    path('logout/', auth_views.LogoutView.as_view(template_name='loginout/logout.html'), name='logout'),
    path('delete/<int:id>', views.delete_confirm, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    #path('login/', auth_views.LoginView.as_view(template_name='loginout/login.html'), name='login'),
    path('login/', views.login_user1, name='login'),
    path('redirect/', TemplateView.as_view(template_name='redirect.html')),
    path('search/',views.scroop, name='search'),
    path('check_username/', views.check_username, name='check-username')
    

  
]