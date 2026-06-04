from django.shortcuts import render

# Create your views here.

def rider_register(request):

    return render(request, 'accounts/rider_register.html')