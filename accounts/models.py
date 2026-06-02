from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    VENDOR = "vendor"
    RIDER = "rider"

    ROLE_CHOICES = [(VENDOR, "Vendor"), (RIDER, "Rider")]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, blank=True, null=True)

    phone = models.CharField(max_length=20, unique=True)

    avatar = models.ImageField(upload_to="users/", blank=True, null=True)

    is_verified = models.BooleanField(default=False)

    language = models.CharField(max_length=10, default="en")

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)




# class RiderProfile(models.Model):

#     BIKE = "bike"
#     CAR = "car"

#     VEHICLE_CHOICES = [(BIKE, "Bike"), (CAR, "Car")]

#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="rider_profile")

#     full_name = models.CharField(max_length=255)

#     phone = models.CharField(max_length=20)

#     profile_photo = models.ImageField(upload_to="riders/", blank=True, null=True)

#     iqama_number = models.CharField(max_length=50, blank=True)

#     driving_license_number = models.CharField(max_length=100, blank=True)

#     vehicle_type = models.CharField(max_length=20, choices=VEHICLE_CHOICES, default=BIKE)

#     vehicle_plate_number = models.CharField(max_length=50, blank=True)

#     is_online = models.BooleanField(default=False)

#     is_available = models.BooleanField(default=True)

#     is_approved = models.BooleanField(default=False)




# class VendorProfile(models.Model):

#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="vendor_profile")

#     restaurant_name = models.CharField(max_length=255)

#     owner_name = models.CharField(max_length=255)

#     phone = models.CharField(max_length=20)

#     logo = models.ImageField(upload_to="vendors/logos/", blank=True, null=True)

#     cover_image = models.ImageField(upload_to="vendors/covers/", blank=True, null=True)

#     commercial_registration_number = models.CharField(max_length=100, blank=True)

#     vat_number = models.CharField(max_length=100, blank=True)

#     address = models.TextField()

#     city = models.CharField(max_length=100)

#     is_open = models.BooleanField(default=False)

#     is_approved = models.BooleanField(default=False)


