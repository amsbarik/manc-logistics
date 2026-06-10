from django.urls import path 
from .import views

urlpatterns = [
    path('vendors/', views.vendors, name='vendors'),
   
    # food category  
    path('food-categories/', views.food_category_list, name='food_category_list'),
    path('food-category/form/', views.food_category_create_or_update, name='food_category_create'),
    path('food-category/update/<int:pk>/', views.food_category_create_or_update, name='food_category_update'),

    # vendor  
    path('vendors/', views.vendor_list, name='vendor_list'),
    path('vendor/form/', views.vendor_create_or_update, name='vendor_create'),
    path('vendor/update/<int:pk>/', views.vendor_create_or_update, name='vendor_update'),
    
    # vendor branch 
    path('vendor-branch/', views.vendor_branch_list, name='vendor_branch_list'),
    path('vendor-branch/form/', views.vendor_branch_create_or_update, name='vendor_branch_create'),
    path('vendor-branch/update/<int:pk>/', views.vendor_branch_create_or_update, name='vendor_branch_update'),
    
]

