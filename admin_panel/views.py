from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import user_passes_test, login_required
from .forms import SiteSettingForm

from accounts.permissions import is_admin
from .models import SiteSetting


# Create your views here.

# admin dashboard view
@login_required
@user_passes_test(is_admin)
def dashboard(request):
    return render(request, 'admin_panel/dashboard.html')



# site settings ////////////////
@login_required
@user_passes_test(is_admin)
def site_setting_view(request):
    setting = SiteSetting.objects.first()  # Get the existing one or None
    if request.method == 'POST':
        form = SiteSettingForm(request.POST, request.FILES, instance=setting)
        if form.is_valid():
            form.save()
            return redirect('site_setting')
    else:
        form = SiteSettingForm(instance=setting)
    
    return render(request, 'admin_panel/site_setting_form.html', {'form': form})





























