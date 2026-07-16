from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

from accounts.models import RiderProfile

from .forms import RiderForm, RiderStatusForm

from accounts.permissions import is_admin



# Create your views here.

def riders(request):
    riders = RiderProfile.objects.filter(status='active')
    return render(request, 'rider/riders.html', {'riders': riders})





# /////////////////////////////////////////////////////////////////////////////////////////
# admin panel 
from django.contrib.auth import get_user_model

User = get_user_model()

# rider create & update form view 
@login_required
@user_passes_test(is_admin)
def rider_create_or_update(request, pk=0):

    rider = None


    if pk:
        rider = get_object_or_404(
            RiderProfile,
            id=pk
        )


    if request.method == "POST":

        form = RiderForm(
            request.POST,
            request.FILES,
            instance=rider
        )


        if form.is_valid():

            rider = form.save(
                commit=False
            )


            if not rider.user:

                user = User.objects.create_user(
                    username=rider.iqama_number,
                    role=User.RIDER
                )

                rider.user = user


            rider.save()


            messages.success(
                request,
                "Rider updated successfully."
            )


            return redirect(
                request.POST.get("next")
            )


    else:

        form = RiderForm(
            instance=rider
        )


    return render(
        request,
        "rider/admin/rider_form.html",
        {
            "form": form,
        }
    )



# @login_required
# @user_passes_test(is_admin)
# def rider_create_or_update(request, pk=0):

#     if pk == 0:
#         rider = None
#     else:
#         rider = get_object_or_404(RiderProfile, id=pk)

#     if request.method == "POST":

#         form = RiderForm(request.POST,  request.FILES, instance=rider)

#         if form.is_valid():
#             form.save()

#             messages.success(request, "Rider created successfully.")

#             return redirect(request.POST.get("next") )

#     else:

#         form = RiderForm(instance=rider)


#     return render(request,"rider/admin/rider_form.html",{"form": form})


# @login_required
# @user_passes_test(is_admin)
# def rider_create_or_update(request, pk=0):
    
#     if request.method == 'GET':
#         if pk == 0:
#             form = RiderForm()
#         else:
#             rider = RiderProfile.objects.get(id=pk)
#             form = RiderForm(instance=rider)
            
#         return render(request, 'rider/admin/rider_form.html', {'form': form})
    
#     else:
#         if pk == 0:
#             form = RiderForm(request.POST, request.FILES)
#         else:
#             rider = RiderProfile.objects.get(id=pk)
#             form = RiderForm(request.POST, request.FILES, instance=rider)

#         if form.is_valid():
#             form.save()
            
#         return redirect('hero_slider_list')






# admin rider manage views 
def rider_status_list(request, status, template):

    riders = RiderProfile.objects.select_related("user").filter(status=status).order_by("-created_at")

    if request.method == "POST":

        rider_id = request.POST.get("rider_id")

        rider = get_object_or_404(RiderProfile, id=rider_id)

        form = RiderStatusForm(request.POST, instance=rider)

        if form.is_valid():
            form.save()

            messages.success(request, "Rider status updated successfully.")

            return redirect(request.path)

    else:

        form = RiderStatusForm()


    return render(request, template, {"riders": riders, "form": form})



@login_required
@user_passes_test(is_admin)
def pending_riders(request):
    return rider_status_list(request, RiderProfile.PENDING, "rider/admin/pending_riders.html")


@login_required
@user_passes_test(is_admin)
def under_review_riders(request):
    return rider_status_list(request, RiderProfile.UNDER_REVIEW, "rider/admin/under_review_riders.html")


@login_required
@user_passes_test(is_admin)
def interview_riders(request):
    return rider_status_list(request, RiderProfile.INTERVIEW, "rider/admin/interview_riders.html")


@login_required
@user_passes_test(is_admin)
def active_riders(request):
    return rider_status_list(request, RiderProfile.ACTIVE, "rider/admin/active_riders.html")


@login_required
@user_passes_test(is_admin)
def suspended_riders(request):
    return rider_status_list(request, RiderProfile.SUSPENDED, "rider/admin/suspended_riders.html")


@login_required
@user_passes_test(is_admin)
def inactive_riders(request):
    return rider_status_list(request, RiderProfile.INACTIVE, "rider/admin/inactive_riders.html")


@login_required
@user_passes_test(is_admin)
def rejected_riders(request):
    return rider_status_list(request, RiderProfile.REJECTED, "rider/admin/rejected_riders.html")