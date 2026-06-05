from django.urls import path 
from .import views

urlpatterns = [
    path('', views.index, name='index'),

    # admin panel urls ////////////////////////////////////////////////////////////////////////////////////
    # hero sliders urls 
    path('hero-sliders/', views.hero_slider_list, name='hero_slider_list'),
    path('hero-slider/form/', views.hero_slider_form, name='hero_slider_create'),
    path('hero-slider/update/<int:pk>/', views.hero_slider_form, name='hero_slider_update'),
    # path('hero-slider/delete/<int:pk>/', views.hero_slider_delete, name='hero_slider_delete'),

    # partner 
    path('partners/', views.partner_list, name='partner_list'),
    path('partner/form/', views.partner_form, name='partner_create'),
    path('partner/update/<int:pk>/', views.partner_form, name='partner_update'),

    # why choose us 
    path('benefits/', views.why_choose_us_list, name='why_choose_us_list'),
    path('benefit/form/', views.why_choose_us_form, name='why_choose_us_create'),
    path('benefit/update/<int:pk>/', views.why_choose_us_form, name='why_choose_us_update'),
    
]


# from django.urls import path 
# from .import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('newsletter/', views.newsletter, name='newsletter'),
#     path('banners/', views.create_or_update_banner, name='create_or_update_banner'),

#     path('contact/', views.contact, name='contact'),
    
#     path('messages/', views.contact_list, name='contact_list'),
#     path('message/update/<int:contact_id>/', views.message_status_update, name='message_status_update'),

#     path('about-us/', views.about_us, name='about_us'),
#     path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
#     path('refund-cancellation/', views.refund_cancellation, name='refund_cancellation'),
#     path('terms-and-conditions/', views.terms_conditions, name='terms_conditions'),
    
#     
#     # top_link urls
#     path('toplink-form/', views.top_link_form, name='top_link_form'),


#     path('newsletters/', views.newsletter_all, name='newsletter_all'),
#     path('newsletter/form/', views.newsletter_form, name='newsletter_form'),
#     path('newsletter/update/<int:pk>/', views.newsletter_form, name='newsletter_update'),
#     # path('newsletter/delete/<int:pk>/', views.newsletter_delete, name='newsletter_delete'),

#     path('faqs/', views.faq_all, name='faq_all'),
#     path('faq/form/', views.faq_form, name='faq_form'),
#     path('faq/update/<int:pk>/', views.faq_form, name='faq_update'),

#   
# ]

