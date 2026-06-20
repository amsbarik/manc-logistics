from django.urls import path 
from .import views

urlpatterns = [
    path('contact-us/', views.contact_us, name='contact_us'),
   
#     path('contact/', views.contact, name='contact'),
    
# #     path('messages/', views.contact_list, name='contact_list'),
# #     path('message/update/<int:contact_id>/', views.message_status_update, name='message_status_update'),
    
]

