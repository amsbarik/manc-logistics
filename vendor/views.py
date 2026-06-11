from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib import messages

from accounts.permissions import is_admin

from .models import FoodCategory, Vendor, VendorBranch
from .forms import FoodCategoryForm, VendorForm, VendorBranchForm



# Create your views here.

def vendors(request):

    vendor_branches = VendorBranch.objects.filter(is_active=True).order_by('order')
    return render(request, 'vendor/vendors.html', {'vendor_branches': vendor_branches})







# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# admin panel views start here ///////////////////////////////////////////

# Food category view 
@login_required
@user_passes_test(is_admin)
def food_category_list(request):
    food_categories = FoodCategory.objects.all()
    
    return render(request, 'vendor/admin/food_category_list.html', {'food_categories': food_categories})


# Food Category create & update form view 
@login_required
@user_passes_test(is_admin)
def food_category_create_or_update(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = FoodCategoryForm()
        else:
            food_category = FoodCategory.objects.get(id=pk)
            form = FoodCategoryForm(instance=food_category)
            
        return render(request, 'vendor/admin/food_category_form.html', {'form': form})
    
    else:
        if pk == 0:
            form = FoodCategoryForm(request.POST, request.FILES)
        else:
            food_category = FoodCategory.objects.get(id=pk)
            form = FoodCategoryForm(request.POST, request.FILES, instance=food_category)

        if form.is_valid():
            form.save()
            
        return redirect('food_category_list')


# ///////////////////////////////////////////////////////////////////////////////// 
# Vendor view 
@login_required
@user_passes_test(is_admin)
def vendor_list(request):
    vendors = Vendor.objects.all()
    
    return render(request, 'vendor/admin/vendor_list.html', {'vendors': vendors})


# vendor create & update form view 
@login_required
@user_passes_test(is_admin)
def vendor_create_or_update(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = VendorForm()
        else:
            vendor = Vendor.objects.get(id=pk)
            form = VendorForm(instance=vendor)
            
        return render(request, 'vendor/admin/vendor_form.html', {'form': form})
    
    else:
        if pk == 0:
            form = VendorForm(request.POST, request.FILES)
        else:
            vendor = Vendor.objects.get(id=pk)
            form = VendorForm(request.POST, request.FILES, instance=vendor)

        if form.is_valid():
            form.save()
            
        return redirect('vendor_list')


# ///////////////////////////////////////////////////////////////////////////////// 
# Vendor branch view 
@login_required
@user_passes_test(is_admin)
def vendor_branch_list(request):
    vendor_branches = VendorBranch.objects.all()
    
    return render(request, 'vendor/admin/vendor_branch_list.html', {'vendor_branches': vendor_branches})


# vendor branch create & update form view 
@login_required
@user_passes_test(is_admin)
def vendor_branch_create_or_update(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = VendorBranchForm()
        else:
            branch = VendorBranch.objects.get(id=pk)
            form = VendorBranchForm(instance=branch)
            
        return render(request, 'vendor/admin/vendor_branch_form.html', {'form': form})
    
    else:
        if pk == 0:
            form = VendorBranchForm(request.POST, request.FILES)
        else:
            branch = VendorBranch.objects.get(id=pk)
            form = VendorBranchForm(request.POST, request.FILES, instance=branch)

        if form.is_valid():
            form.save()
            
        return redirect('vendor_branch_list')


# @login_required
# @user_passes_test(is_admin)
# def vendor_branch_create_or_update(request, pk=0):

#     if request.method == 'POST':

#         if pk == 0:
#             form = VendorBranchForm(request.POST, request.FILES)
#         else:
#             branch = VendorBranch.objects.get(id=pk)
#             form = VendorBranchForm(
#                 request.POST,
#                 request.FILES,
#                 instance=branch
#             )

#         if form.is_valid():
#             if form.is_valid():
#                 form.save()
#                 return redirect('vendor_branch_list')

#             print(form.errors)
#             print(form.non_field_errors())

#         print(form.errors)  # Debug

#     else:
#         if pk == 0:
#             form = VendorBranchForm()
#         else:
#             branch = VendorBranch.objects.get(id=pk)
#             form = VendorBranchForm(instance=branch)

#     return render(
#         request,
#         'vendor/admin/vendor_branch_form.html',
#         {'form': form}
#     )
