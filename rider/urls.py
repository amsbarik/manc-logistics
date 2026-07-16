from django.urls import path 
from .import views

urlpatterns = [

    path('riders/', views.riders, name='riders'),

    # admin urls 
    path("riders/pending/", views.pending_riders, name="pending_riders"),
    path("riders/under-review/", views.under_review_riders, name="under_review_riders"),
    path("riders/interview/", views.interview_riders, name="interview_riders"),
    path("riders/active/", views.active_riders, name="active_riders"),
    path("riders/suspended/", views.suspended_riders, name="suspended_riders"),
    path("riders/inactive/", views.inactive_riders, name="inactive_riders"),
    path("riders/rejected/", views.rejected_riders, name="rejected_riders"),

    path("rider/create/", views.rider_create_or_update, name="rider_create"),
    path('rider/update/<int:pk>/', views.rider_create_or_update, name='rider_update'),

    path('rider/recruitment/', views.rider_recruitment_manage, name='rider_recruitment_manage'),

    # path('rider/update/<int:pk>/', views.rider_list, name='rider_update'),
    # path("riders/<str:status>/", views.rider_manage, name="rider_manage_status"),
   
    
]



