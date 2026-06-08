from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib import messages

from django.utils import timezone
from datetime import timedelta

from accounts.permissions import is_admin

from .models import ExpertTeam
from .forms import ExpertTeamForm



# Create your views here.

def about_us(request):
    pass





# ////////////////////////////////////////////////////
# admin views start here  //////////////////////////////////////////////////////////

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







