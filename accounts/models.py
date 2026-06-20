from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings



from core.models import BaseModel, City


# User 
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


# RiderProfile
class RiderProfile(BaseModel):

    PENDING = "pending"
    UNDER_REVIEW = "under_review"
    # DOCUMENT_VERIFICATION = "document_verification"
    INTERVIEW = "interview"
    # TRAINING = "training"
    ACTIVE = "active"
    SUSPENDED = "suspended"
    REJECTED = "rejected"
    INACTIVE = "inactive"


    STATUS_CHOICES = [
        (PENDING, "Pending"),
        (UNDER_REVIEW, "Under Review"),
        (INTERVIEW, "Interview"),
        (ACTIVE, "Active"),
        (SUSPENDED, "Suspended"),
        (INACTIVE, "Inactive"),
        (REJECTED, "Rejected"),
    ]


    CAR = "with_car"
    WITHOUT = "without_car"

    VEHICLE_CHOICES = [
        (CAR, "With Car"),
        (WITHOUT, "Without Car"),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="rider_profile")

    # Personal Information
    full_name = models.CharField(max_length=150)
    nationality = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_photo = models.ImageField( upload_to="riders/profile/", blank=True,  null=True)

    # Location
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='city_riders')
    address = models.TextField(blank=True)

    # Saudi Documents
    iqama_number = models.CharField(max_length=50, unique=True)
    iqama_expired_date = models.DateField()
    driving_license_number = models.CharField(max_length=100, unique=True)

    # Vehicle
    vehicle_type = models.CharField(max_length=30, choices=VEHICLE_CHOICES)
    vehicle_plate_number = models.CharField(max_length=50, blank=True)

    # System
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,default=PENDING)
    is_online = models.BooleanField(default=False)
    is_available = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)


    def __str__(self):
        return self.full_name




# Vendor Profile
class VendorProfile(BaseModel):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="vendor_profile")

    business_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='vendors/logos/', blank=True, null=True )
    cover_photo = models.ImageField( upload_to='vendors/covers/',  blank=True, null=True )

    trade_license = models.FileField(  upload_to='vendors/trade-licenses/', blank=True, null=True)
    vat_number = models.CharField(max_length=100, blank=True)

    city = models.ForeignKey('core.City', on_delete=models.PROTECT, related_name='city_vendors')
    address = models.CharField( max_length=255, blank=True)
    description = models.TextField(blank=True)

    owner_name = models.CharField(max_length=255, blank=True)
    owner_phone = models.CharField(max_length=20, blank=True)

    is_open = models.BooleanField(default=False)

    is_approved = models.BooleanField(default=False)


    def __str__(self):
        return self.business_name




