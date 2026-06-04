from django.shortcuts import render

# Create your views here.


def index(request):

  
    return render(request, 'core/index.html')











# ///////////////////////////////////////////////
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib import messages

from django.utils import timezone
from datetime import timedelta

from apps.user_auth.views import is_superuser

from .forms import ContactForm, TopSliderForm, NewsletterForm
from .models import Contact, TopLink, TopSlider, Newsletter, Banner, FAQ, Partner
from .forms import ContactForm, ContactStatusForm, TopLinkForm, BannerForm, FAQForm, PartnerForm

from apps.university.models import University, Department, Discipline
from apps.user_auth.models import Testimonial
from apps.pricing_plan.models import PricingPlan, PlanFeature



# Create your views here.
def index(request):
    # Fetch active top sliders
    top_sliders = TopSlider.objects.filter(is_active=True).order_by('order')
    top_links = TopLink.objects.first()

    # universities = University.objects.filter(is_top=True).order_by('order')[:15]
    universities = University.objects.order_by('order')[:15]
    testimonials = Testimonial.objects.filter(is_active=True).order_by('order')[:8]
    banner = Banner.objects.first()
    faqs = FAQ.objects.filter(is_active=True).order_by('order')
    partners = Partner.objects.filter(is_active=True).order_by('order')[:10]

    # disciplines
    disciplines = Discipline.objects.filter(is_active=True).order_by('-order').all()
    # PricingPlan
    pricing_plans = PricingPlan.objects.prefetch_related('features').filter(is_active=True).order_by('order').all()
   
    context = {
        'top_sliders': top_sliders,
        'top_links': top_links,
        'universities': universities,
        'testimonials': testimonials,
        'banner': banner,
        'faqs': faqs,
        'partners': partners,

        'disciplines': disciplines,
        'pricing_plans': pricing_plans,
    }

    return render(request, 'core/index.html', context)



#newsletter 
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






def about_us(request):
    return render(request, 'core/about_us.html')

def privacy_policy(request):
    return render(request, 'core/privacy_policy.html')


def refund_cancellation(request):
    return render(request, 'core/refund_cancellation.html')


def terms_conditions(request):
    return render(request, 'core/terms_conditions.html')







# admin panel views here ///////////////////////////////////
# Top all slider view 
@login_required
@user_passes_test(is_superuser)
def top_slider_all(request):
    top_sliders = TopSlider.objects.order_by('created_at').all()
    
    return render(request, 'admin_panel/core/top_slider_all.html', {'top_sliders': top_sliders})


# TopSlider create & update form view 
@login_required
@user_passes_test(is_superuser)
def top_slider_form(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = TopSliderForm()
        else:
            top_slider = TopSlider.objects.get(id=pk)
            form = TopSliderForm(instance=top_slider)
            
        return render(request, 'admin_panel/core/top_slider_form.html', {'form': form})
    
    else:
        if pk == 0:
            form = TopSliderForm(request.POST, request.FILES)
        else:
            top_slider = TopSlider.objects.get(id=pk)
            form = TopSliderForm(request.POST, request.FILES, instance=top_slider)

        if form.is_valid():
            form.save()
            
        return redirect('top_slider_all')


# TopSlider delete view 
# @login_required
# @user_passes_test(is_superuser)
# def top_slider_delete(request, pk):
#     top_silder = TopSlider.objects.get(id=pk)
#     top_silder.delete()
#     return redirect('top_slider_all')




# TopLink view
@login_required
@user_passes_test(is_superuser)
def top_link_form(request):
    top_link = TopLink.objects.first()  # Get the existing one or None
    if request.method == 'POST':
        form = TopLinkForm(request.POST, request.FILES, instance=top_link)
        if form.is_valid():
            form.save()
            return redirect('top_link_form')
    else:
        form = TopLinkForm(instance=top_link)
    
    return render(request, 'admin_panel/core/top_link_form.html', {'form': form})





# Banners view 
@login_required
@user_passes_test(is_superuser)
def create_or_update_banner(request):
    # Get the first banner instance, or create a new one if none exists
    banner_instance = Banner.objects.first()

    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES, instance=banner_instance)
        if form.is_valid():
            form.save()
            messages.success(request, "Banner updated successfully.")
            return redirect('create_or_update_banner')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = BannerForm(instance=banner_instance)

    return render(request, 'admin_panel/core/banner_form.html', {'form': form})







# newsletter_all views
@login_required
@user_passes_test(is_superuser)
def newsletter_all(request):
    newsletters = Newsletter.objects.order_by('subscribed_at').all()
    
    return render(request, 'admin_panel/core/newsletter_all.html', {'newsletters': newsletters})


@login_required
@user_passes_test(is_superuser)
def newsletter_form(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = NewsletterForm()
        else:
            newsletter = Newsletter.objects.get(id=pk)
            form = NewsletterForm(instance=newsletter)
            
        return render(request, 'admin_panel/core/newsletter_form.html', {'form': form})
    
    else:
        if pk == 0:
            form = NewsletterForm(request.POST, request.FILES)
        else:
            newsletter = Newsletter.objects.get(id=pk)
            form = NewsletterForm(request.POST, request.FILES, instance=newsletter)

        if form.is_valid():
            form.save()
            
        return redirect('newsletter_all')
    

# newsletter_delete
# @login_required
# @user_passes_test(is_superuser)
# def newsletter_delete(request, pk):
#     newsletter = Newsletter.objects.get(id=pk)
#     newsletter.delete()
#     return redirect('newsletter_all')




# contact views
def contact(request):
    # contact = Contact.objects.all()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')  # Redirect to avoid resubmission on refresh
    else:
        form = ContactForm()
        
    # Pass form fields individually
    context = {
        'user_name': form['user_name'],
        'user_mobile': form['user_mobile'],
        'user_email': form['user_email'],
        'user_message': form['user_message']
    }
    
    return render(request, 'core/contact.html', context)









# admin view start here 
# contact list view 
@login_required
@user_passes_test(is_superuser)
def contact_list(request):
    messages = Contact.objects.order_by('created_at').all()
    
    return render(request, 'admin_panel/core/messages.html', {'messages': messages})



@login_required
@user_passes_test(is_superuser)
def message_status_update(request, contact_id):
    
    messages = Contact.objects.all()
    message = get_object_or_404(Contact, id=contact_id)
    
    if request.method == 'POST':
        form = ContactStatusForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Message status updated successfully.')
            return redirect('messages')
        
    else:
        form = ContactStatusForm(instance=message)
    
    return render(request, 'admin_panel/core/messages.html', {'form': form, 'messages': messages})






# FAQs view 
@login_required
@user_passes_test(is_superuser)
def faq_all(request):
    faqs = FAQ.objects.order_by('created_at').all()
    
    return render(request, 'admin_panel/core/faq_all.html', {'faqs': faqs})


# FAQs create & update form view 
@login_required
@user_passes_test(is_superuser)
def faq_form(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = FAQForm()
        else:
            faq = FAQ.objects.get(id=pk)
            form = FAQForm(instance=faq)
            
        return render(request, 'admin_panel/core/faq_form.html', {'form': form})
    
    else:
        if pk == 0:
            form = FAQForm(request.POST, request.FILES)
        else:
            faq = FAQ.objects.get(id=pk)
            form = FAQForm(request.POST, request.FILES, instance=faq)

        if form.is_valid():
            form.save()
            
        return redirect('faq_all')




# Partner_list view 
@login_required
@user_passes_test(is_superuser)
def partner_list(request):
    partners = Partner.objects.order_by('created_at').all()
    
    return render(request, 'admin_panel/core/partner_list.html', {'partners': partners})


# Partner_list create & update form view 
@login_required
@user_passes_test(is_superuser)
def partner_form(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = PartnerForm()
        else:
            partner = Partner.objects.get(id=pk)
            form = PartnerForm(instance=partner)
            
        return render(request, 'admin_panel/core/partner_form.html', {'form': form})
    
    else:
        if pk == 0:
            form = PartnerForm(request.POST, request.FILES)
        else:
            partner = Partner.objects.get(id=pk)
            form = PartnerForm(request.POST, request.FILES, instance=partner)

        if form.is_valid():
            form.save()
            
        return redirect('partner_list')


