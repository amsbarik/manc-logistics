from django.urls import path 
from .import views

urlpatterns = [
    path('services/', views.services, name='services'),
   
    # Service 
    path('Services/', views.service_list, name='service_list'),
    path('Service/form/', views.service_create_or_update, name='service_create'),
    path('Service/update/<int:pk>/', views.service_create_or_update, name='service_update'),
    
]

