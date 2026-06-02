from django.urls import path 
from .import views

urlpatterns = [
    path('', views.index, name='index'),
   
#     # partner 
#     path('partners/', views.partner_list, name='partner_list'),
#     path('partner/form/', views.partner_form, name='partner_form'),
#     path('partner/update/<int:pk>/', views.partner_form, name='partner_update'),
    
]

