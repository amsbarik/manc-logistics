from django.urls import path 
from .import views


urlpatterns = [
    path('about-us', views.about_us, name='about_us'),

    # about 
    path('about/', views.about_create_or_update, name='about_create_or_update'),
   
    # expert_team 
    path('expert-teams/', views.expert_team_list, name='expert_team_list'),
    path('expert-team/form/', views.expert_team_create_or_update, name='expert_team_create'),
    path('expert-team/update/<int:pk>/', views.expert_team_create_or_update, name='expert_team_update'),

    # working process 
    path('working-process/', views.working_process_list, name='working_process_list'),
    path('working-process/form/', views.working_process_create_or_update, name='working_process_create'),
    path('working-process/update/<int:pk>/', views.working_process_create_or_update, name='working_process_update'),
    
]

