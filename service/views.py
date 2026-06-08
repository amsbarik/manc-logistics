from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

from accounts.permissions import is_admin

from .models import Service
from .forms import ServiceForm

# Create your views here.

def services(request):

    services = Service.objects.filter(is_active=True).order_by('order')

    context = {
        'services': services
    }

    return render(request, 'service/services.html', context)





# //////////////////////////////////////////
# Service list  
@login_required
@user_passes_test(is_admin)
def service_list(request):
    services = Service.objects.all()
    
    return render(request, 'service/admin/service_list.html', {'services': services})


# service create & update view 
@login_required
@user_passes_test(is_admin)
def service_create_or_update(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = ServiceForm()
        else:
            service = Service.objects.get(id=pk)
            form = ServiceForm(instance=service)
            
        return render(request, 'service/admin/service_form.html', {'form': form})
    
    else:
        if pk == 0:
            form = ServiceForm(request.POST, request.FILES)
        else:
            service = Service.objects.get(id=pk)
            form = ServiceForm(request.POST, request.FILES, instance=service)

        if form.is_valid():
            form.save()
            
        return redirect('service_list')

