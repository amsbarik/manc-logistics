from django.urls import path
from .import views 

urlpatterns = [
    path('login/', views.admin_login, name='admin_login'),
    path('logout/', views.admin_logout, name='admin_logout'),
    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('settings/', views.site_setting_view, name='site_setting'),
    
]


