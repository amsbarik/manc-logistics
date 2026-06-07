from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib import messages

from django.utils import timezone
from datetime import timedelta


from accounts.permissions import is_admin
from service.models import Service

from .models import HeroSlider, Partner, LeadershipMessage, WhyChooseUs, FAQ, Newsletter
from .forms import HeroSliderForm, PartnerForm, LeadershipMessageForm, WhyChooseUsForm, FAQForm, NewsletterForm



# Create your views here.


def index(request):

    hero_sliders = HeroSlider.objects.filter(is_active=True).order_by('order')
    partners = Partner.objects.filter(is_active=True).order_by('order')[:20]
    services = Service.objects.filter(is_active=True).order_by('order')[:4]
    leadership_message = LeadershipMessage.objects.first()
    benefits = WhyChooseUs.objects.filter(is_active=True).order_by('order')[:6]
    # faqs = FAQ.objects.filter(is_active=True).order_by('order')
    faqs_rider = FAQ.objects.filter(is_active=True, faq_type=FAQ.FAQType.RIDER).order_by('order')
    faqs_merchant = FAQ.objects.filter(is_active=True, faq_type=FAQ.FAQType.MERCHANT).order_by('order')



    context = {
        'hero_sliders': hero_sliders,
        'partners': partners,
        'services': services,
        'leadership_message': leadership_message,
        'benefits': benefits,
        'faqs_rider': faqs_rider,
        'faqs_merchant': faqs_merchant,
    }
  
    return render(request, 'core/index.html', context)






# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# admin panel views start here ///////////////////////////////////////////

# Top all slider view 
@login_required
@user_passes_test(is_admin)
def hero_slider_list(request):
    hero_sliders = HeroSlider.objects.all()
    
    return render(request, 'core/admin/hero_slider_list.html', {'hero_sliders': hero_sliders})


# Hero Slider create & update form view 
@login_required
@user_passes_test(is_admin)
def hero_slider_form(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = HeroSliderForm()
        else:
            hero_slider = HeroSlider.objects.get(id=pk)
            form = HeroSliderForm(instance=hero_slider)
            
        return render(request, 'core/admin/hero_slider_form.html', {'form': form})
    
    else:
        if pk == 0:
            form = HeroSliderForm(request.POST, request.FILES)
        else:
            hero_slider = HeroSlider.objects.get(id=pk)
            form = HeroSliderForm(request.POST, request.FILES, instance=hero_slider)

        if form.is_valid():
            form.save()
            
        return redirect('hero_slider_list')



# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Partner_list view 
@login_required
@user_passes_test(is_admin)
def partner_list(request):
    partners = Partner.objects.all()
    
    return render(request, 'core/admin/partner_list.html', {'partners': partners})


# Partner create & update form view 
@login_required
@user_passes_test(is_admin)
def partner_form(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = PartnerForm()
        else:
            partner = Partner.objects.get(id=pk)
            form = PartnerForm(instance=partner)
            
        return render(request, 'core/admin/partner_form.html', {'form': form})
    
    else:
        if pk == 0:
            form = PartnerForm(request.POST, request.FILES)
        else:
            partner = Partner.objects.get(id=pk)
            form = PartnerForm(request.POST, request.FILES, instance=partner)

        if form.is_valid():
            form.save()
            
        return redirect('partner_list')



# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# leadership messages create & update view 
@login_required
@user_passes_test(is_admin)
def leadership_message(request):
    message = LeadershipMessage.objects.first()  # Get the existing one or None
    if request.method == 'POST':
        form = LeadershipMessageForm(request.POST, request.FILES, instance=message)
        if form.is_valid():
            form.save()
            return redirect('leadership_message')
    else:
        form = LeadershipMessageForm(instance=message)
    
    return render(request, 'core/admin/leadership_message_form.html', {'form': form})


# ////////////////////////////////////////////////////////////////////////////
# WhyChooseUs  view 
@login_required
@user_passes_test(is_admin)
def why_choose_us_list(request):
    benefits = WhyChooseUs.objects.all()
    
    return render(request, 'core/admin/why_choose_us_list.html', {'benefits': benefits})


# WhyChooseUs create & update form view 
@login_required
@user_passes_test(is_admin)
def why_choose_us_form(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = WhyChooseUsForm()
        else:
            benefit = WhyChooseUs.objects.get(id=pk)
            form = WhyChooseUsForm(instance=benefit)
            
        return render(request, 'core/admin/why_choose_us_form.html', {'form': form})
    
    else:
        if pk == 0:
            form = WhyChooseUsForm(request.POST, request.FILES)
        else:
            benefit = WhyChooseUs.objects.get(id=pk)
            form = WhyChooseUsForm(request.POST, request.FILES, instance=benefit)

        if form.is_valid():
            form.save()
            
        return redirect('why_choose_us_list')


# /////////////////////////////////////////////////////////////////
# FAQs view 
@login_required
@user_passes_test(is_admin)
def faq_list(request):
    faqs = FAQ.objects.all()
    
    return render(request, 'core/admin/faq_list.html', {'faqs': faqs})


# FAQs create & update form view 
@login_required
@user_passes_test(is_admin)
def faq_create_or_update(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = FAQForm()
        else:
            faq = FAQ.objects.get(id=pk)
            form = FAQForm(instance=faq)
            
        return render(request, 'core/admin/faq_form.html', {'form': form})
    
    else:
        if pk == 0:
            form = FAQForm(request.POST, request.FILES)
        else:
            faq = FAQ.objects.get(id=pk)
            form = FAQForm(request.POST, request.FILES, instance=faq)

        if form.is_valid():
            form.save()
            
        return redirect('faq_list')


# ////////////////////////////////////////////////////////////////// 
#newsletter from user
def newsletter(request):
    if request.method == "POST":
        news_email = request.POST.get("news-email")  # Get email from input field
        
        if not news_email:
            messages.error(request, "Email field cannot be empty.")
        else:
            if Newsletter.objects.filter(email=news_email).exists():
                messages.warning(request, "You are already subscribed.")
            else:
                Newsletter.objects.create(email=news_email)
                messages.success(request, "Thank you for subscribing!")
        
        return redirect('index')  # Reload the page with messages

    return render(request, 'core/index.html')  # Render template


# from admin ///////////////////
# newsletter list views
@login_required
@user_passes_test(is_admin)
def newsletter_list(request):
    newsletters = Newsletter.objects.all()
    
    return render(request, 'core/admin/newsletter_list.html', {'newsletters': newsletters})


@login_required
@user_passes_test(is_admin)
def newsletter_form(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = NewsletterForm()
        else:
            newsletter = Newsletter.objects.get(id=pk)
            form = NewsletterForm(instance=newsletter)
            
        return render(request, 'core/admin/newsletter_form.html', {'form': form})
    
    else:
        if pk == 0:
            form = NewsletterForm(request.POST, request.FILES)
        else:
            newsletter = Newsletter.objects.get(id=pk)
            form = NewsletterForm(request.POST, request.FILES, instance=newsletter)

        if form.is_valid():
            form.save()
            
        return redirect('newsletter_list')
    










# # admin dashboard view
# @login_required
# @user_passes_test(is_superuser)
# def site_setting_view(request):
#     setting = SiteSetting.objects.first()  # Get the existing one or None
#     if request.method == 'POST':
#         form = SiteSettingForm(request.POST, request.FILES, instance=setting)
#         if form.is_valid():
#             form.save()
#             return redirect('site_setting')
#     else:
#         form = SiteSettingForm(instance=setting)
    
#     return render(request, 'admin_panel/site_setting_form.html', {'form': form})



# # ///////////////////////////////////////////////
# before codes 






# def about_us(request):
#     return render(request, 'core/about_us.html')

# def privacy_policy(request):
#     return render(request, 'core/privacy_policy.html')


# def refund_cancellation(request):
#     return render(request, 'core/refund_cancellation.html')


# def terms_conditions(request):
#     return render(request, 'core/terms_conditions.html')







# # admin panel views here ///////////////////////////////////




# # TopLink view
# @login_required
# @user_passes_test(is_superuser)
# def top_link_form(request):
#     top_link = TopLink.objects.first()  # Get the existing one or None
#     if request.method == 'POST':
#         form = TopLinkForm(request.POST, request.FILES, instance=top_link)
#         if form.is_valid():
#             form.save()
#             return redirect('top_link_form')
#     else:
#         form = TopLinkForm(instance=top_link)
    
#     return render(request, 'admin_panel/core/top_link_form.html', {'form': form})





# # Banners view 
# @login_required
# @user_passes_test(is_superuser)
# def create_or_update_banner(request):
#     # Get the first banner instance, or create a new one if none exists
#     banner_instance = Banner.objects.first()

#     if request.method == 'POST':
#         form = BannerForm(request.POST, request.FILES, instance=banner_instance)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Banner updated successfully.")
#             return redirect('create_or_update_banner')
#         else:
#             messages.error(request, "Please correct the errors below.")
#     else:
#         form = BannerForm(instance=banner_instance)

#     return render(request, 'admin_panel/core/banner_form.html', {'form': form})








# # contact views
# def contact(request):
#     # contact = Contact.objects.all()
    
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the data to the database
#             messages.success(request, 'Your message has been sent successfully!')
#             return redirect('contact')  # Redirect to avoid resubmission on refresh
#     else:
#         form = ContactForm()
        
#     # Pass form fields individually
#     context = {
#         'user_name': form['user_name'],
#         'user_mobile': form['user_mobile'],
#         'user_email': form['user_email'],
#         'user_message': form['user_message']
#     }
    
#     return render(request, 'core/contact.html', context)









# # admin view start here 
# # contact list view 
# @login_required
# @user_passes_test(is_superuser)
# def contact_list(request):
#     messages = Contact.objects.order_by('created_at').all()
    
#     return render(request, 'admin_panel/core/messages.html', {'messages': messages})



# @login_required
# @user_passes_test(is_superuser)
# def message_status_update(request, contact_id):
    
#     messages = Contact.objects.all()
#     message = get_object_or_404(Contact, id=contact_id)
    
#     if request.method == 'POST':
#         form = ContactStatusForm(request.POST, instance=message)
#         if form.is_valid():
#             form.save()
#             # messages.success(request, 'Message status updated successfully.')
#             return redirect('messages')
        
#     else:
#         form = ContactStatusForm(instance=message)
    
#     return render(request, 'admin_panel/core/messages.html', {'form': form, 'messages': messages})










