from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages

from django.contrib.auth import get_user_model
from django.db import transaction

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import user_passes_test, login_required

from core.models import City

from .permissions import is_admin
from .forms import CustomAdminLoginForm, RiderStatusForm
from .models import RiderProfile



# Create your views here.

from django.contrib.auth import get_user_model
from django.db import transaction
from django.shortcuts import render, redirect


User = get_user_model()

def rider_register(request):

    if request.method == "POST":

        try:

            with transaction.atomic():

                user = User.objects.create_user(

                    username=request.POST.get("phone"),

                    phone=request.POST.get("phone"),

                    password=request.POST.get("password"),

                    role=User.RIDER
                )


                city_id = request.POST.get("city")
                city_obj = None
                if city_id:
                    city_obj = City.objects.get(id=city_id)
                

                RiderProfile.objects.create(

                    user=user,

                    full_name=request.POST.get("full_name"),

                    nationality=request.POST.get("nationality"),

                    date_of_birth=request.POST.get("date_of_birth") or None,

                    profile_photo=request.FILES.get("profile_photo") or None,


                    city=city_obj,

                    address=request.POST.get("address"),


                    iqama_number=request.POST.get("iqama_number"),

                    iqama_expired_date=request.POST.get("iqama_expired_date"),


                    driving_license_number=request.POST.get("driving_license_number"),


                    vehicle_type=request.POST.get("vehicle_type"),

                    vehicle_plate_number=request.POST.get("vehicle_plate_number"),

                )

                if messages.success:
                    messages.success(request, "Registration completed successfully. Our team will review your information and contact you soon.")
                else:
                    messages.error(request,"We couldn't complete your registration. Please review your information and try again.")

            return redirect("rider_register")


        except Exception as e:

            print("ERROR:", e)
            messages.error(request, str(e))



    cities = City.objects.filter(is_active=True).order_by("name")
    
    context = {
        'cities': cities,
    }

    return render(request, "accounts/rider_register.html", context)






# def rider_register(request):


#     if request.method == "POST":


#         form = RiderRegisterForm(
#             request.POST,
#             request.FILES
#         )


#         if form.is_valid():


#             with transaction.atomic():


#                 user = User.objects.create_user(

#                     username=form.cleaned_data["phone"],

#                     phone=form.cleaned_data["phone"],

#                     password=form.cleaned_data["password"],

#                     role=User.RIDER

#                 )


#                 RiderProfile.objects.create(

#                     user=user,

#                     full_name=form.cleaned_data["full_name"],

#                     nationality=form.cleaned_data["nationality"],

#                     date_of_birth=form.cleaned_data["date_of_birth"],


#                     profile_photo=form.cleaned_data["profile_photo"],


#                     city=form.cleaned_data["city"],

#                     address=form.cleaned_data["address"],


#                     iqama_number=form.cleaned_data["iqama_number"],

#                     iqama_expired_date=form.cleaned_data["iqama_expired_date"],


#                     driving_license_number=form.cleaned_data["driving_license_number"],


#                     vehicle_type=form.cleaned_data["vehicle_type"],


#                     vehicle_plate_number=form.cleaned_data["vehicle_plate_number"],


#                     iqama_image=form.cleaned_data["iqama_image"],

#                     license_image=form.cleaned_data["license_image"],


#                     status=RiderProfile.PENDING

#                 )



#             return redirect(
#                 "rider_success"
#             )



#     else:

#         form = RiderRegisterForm()



#     return render(request, "accounts/rider_register.html", { "form":form })











# admin panel /////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////

# admin login 
def admin_login(request):
    if request.method == 'POST':
        form = CustomAdminLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_superuser:
                login(request, user)
                return redirect('dashboard')
                # return redirect('admin:index') #this django admin panel
    else:
        form = CustomAdminLoginForm()
    return render(request, 'accounts/admin_login.html', {'form': form})


# logout 
@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_logout(request):
    logout(request)
    return redirect('index') 


# ////////////////////////////////////////////////////////////////////////
# rider list 

# rider list view 
@login_required
@user_passes_test(is_admin)
def rider_list(request):
    riders = RiderProfile.objects.all()
    
    return render(request, 'accounts/admin/rider_list.html', {'riders': riders})

























