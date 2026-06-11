from django.urls import path 
from .import views

urlpatterns = [
    path('login/', views.admin_login, name='admin_login'),
    path('logout/', views.admin_logout, name='admin_logout'),
    
    path('rider-register/', views.rider_register, name='rider_register'),
   
#     # partner 
#     path('partners/', views.partner_list, name='partner_list'),
#     path('partner/form/', views.partner_form, name='partner_form'),
#     path('partner/update/<int:pk>/', views.partner_form, name='partner_update'),
    
]

