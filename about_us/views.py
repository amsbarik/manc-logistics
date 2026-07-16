from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib import messages

from django.utils import timezone
from datetime import timedelta

from accounts.permissions import is_admin

from core.models import LeadershipMessage
from rider.models import RiderRecruitment

from .models import About, WorkingProcess, ExpertTeam
from .forms import AboutForm, WorkingProcessForm, ExpertTeamForm



# Create your views here.

def about_us(request):
    
    about_us = About.objects.first()
    leadership_message = LeadershipMessage.objects.first()
    working_process = WorkingProcess.objects.filter(is_active=True).order_by('id')[:3]
    expert_teams = ExpertTeam.objects.filter(is_active=True).order_by('order')[:5]
    join_us = RiderRecruitment.objects.first()

    context = {
        'about_us': about_us,
        'leadership_message': leadership_message,
        'working_process': working_process,
        'expert_teams': expert_teams,
        'join_us': join_us,
    }
    return render(request, 'about_us/about_us.html', context)





# ////////////////////////////////////////////////////
# admin views start here  //////////////////////////////////////////////////////////

# about create & update form view 
def about_create_or_update(request):

    about = About.objects.first()

    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES, instance=about)

        if form.is_valid():
            form.save()

            messages.success(request, 'About section saved successfully.')

            return redirect('about_create_or_update')

    else:
        form = AboutForm(instance=about)

    context = {
        'form': form,
        'object': about,
    }

    return render(request, 'about_us/admin/about_form.html', context)




# //////////////////////////////////////////////////////////////////////////////////
# Expert Team view 
@login_required
@user_passes_test(is_admin)
def expert_team_list(request):
    expert_teams = ExpertTeam.objects.all()
    
    return render(request, 'about_us/admin/expert_team_list.html', {'expert_teams': expert_teams})


# Expert Team create & update form view 
@login_required
@user_passes_test(is_admin)
def expert_team_create_or_update(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = ExpertTeamForm()
        else:
            expert_team = ExpertTeam.objects.get(id=pk)
            form = ExpertTeamForm(instance=expert_team)
            
        return render(request, 'about_us/admin/expert_team_form.html', {'form': form})
    
    else:
        if pk == 0:
            form = ExpertTeamForm(request.POST, request.FILES)
        else:
            expert_team = ExpertTeam.objects.get(id=pk)
            form = ExpertTeamForm(request.POST, request.FILES, instance=expert_team)

        if form.is_valid():
            form.save()
            
        return redirect('expert_team_list')


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////// 

# working process view 
@login_required
@user_passes_test(is_admin)
def working_process_list(request):
    working_process = WorkingProcess.objects.all()
    
    return render(request, 'about_us/admin/working_process_list.html', {'working_process': working_process})


# working process create & update form view 
@login_required
@user_passes_test(is_admin)
def working_process_create_or_update(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = WorkingProcessForm()
        else:
            working_process = WorkingProcess.objects.get(id=pk)
            form = WorkingProcessForm(instance=working_process)
            
        return render(request, 'about_us/admin/working_process_form.html', {'form': form})
    
    else:
        if pk == 0:
            form = WorkingProcessForm(request.POST, request.FILES)
        else:
            working_process = WorkingProcess.objects.get(id=pk)
            form = WorkingProcessForm(request.POST, request.FILES, instance=working_process)

        if form.is_valid():
            form.save()
            
        return redirect('working_process_list')







