from django.urls import path
from .import views 

urlpatterns = [

    path('dashboard/', views.dashboard, name='dashboard'),
    path('settings/', views.site_setting_view, name='site_setting'),
    
]


