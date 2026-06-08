from django.urls import path 
from .import views


urlpatterns = [
    path('', views.about_us, name='about_us'),
   
    # expert_team 
    path('expert-teams/', views.expert_team_list, name='expert_team_list'),
    path('expert-team/form/', views.expert_team_create_or_update, name='expert_team_create'),
    path('expert-team/update/<int:pk>/', views.expert_team_create_or_update, name='expert_team_update'),
    
]

