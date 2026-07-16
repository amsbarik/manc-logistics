from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

from accounts.models import RiderProfile

from .forms import RiderForm, RiderStatusForm

from accounts.permissions import is_admin


from .forms import RiderRecruitmentForm
from .models import RiderRecruitment


# Create your views here.

def riders(request):
    riders = RiderProfile.objects.filter(status='active')
    return render(request, 'rider/riders.html', {'riders': riders})





# /////////////////////////////////////////////////////////////////////////////////////////
# admin panel 


@login_required
@user_passes_test(is_admin)
def rider_recruitment_manage(request):

    rider_recruitment = RiderRecruitment.objects.first()

    if request.method == "POST":

        form = RiderRecruitmentForm(
            request.POST,
            request.FILES,
            instance=rider_recruitment
        )

        if form.is_valid():
            form.save()

            messages.success(request, "Rider recruitment section saved successfully.")

            return redirect("rider_recruitment_manage")

    else:

        form = RiderRecruitmentForm(instance=rider_recruitment)

    context = {
        "form": form,
        "rider_recruitment": rider_recruitment,
    }

    return render(
        request,
        "rider/admin/rider_recruitment_form.html",
        context
    )






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