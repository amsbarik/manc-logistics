from django.db import models
from django.conf import settings


from core.models import BaseModel



# Create your models here.


# Food Category 
class FoodCategory(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name




# Vendor no need this/////////////////
# class Vendor(BaseModel):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vendor_profile')

#     business_name = models.CharField(max_length=255)

#     logo = models.ImageField(upload_to='vendors/logos/', blank=True, null=True )
#     cover_photo = models.ImageField( upload_to='vendors/covers/',  blank=True, null=True )

#     trade_license = models.FileField(  upload_to='vendors/trade-licenses/', blank=True, null=True)
#     description = models.TextField(blank=True)
#     address = models.CharField( max_length=255, blank=True)

#     is_approved = models.BooleanField(default=False)

#     def __str__(self):
#         return self.business_name





# VendorBranch 
class VendorBranch(BaseModel):
    vendor = models.ForeignKey('accounts.VendorProfile', on_delete=models.PROTECT, related_name='branches', blank=True, null=True)
    branch_name = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='vendor-branches/' )
    short_description = models.CharField( max_length=255,  blank=True )
    categories = models.ManyToManyField(FoodCategory, blank=True)
    address = models.CharField(max_length=255)

    # latitude = models.DecimalField( max_digits=9,  decimal_places=6, null=True, blank=True )
    # longitude = models.DecimalField( max_digits=9,  decimal_places=6, null=True, blank=True )

    is_open = models.BooleanField(default=True)

    def __str__(self):
        return self.branch_name
    




