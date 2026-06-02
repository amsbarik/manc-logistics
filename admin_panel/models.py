from django.db import models

# Create your models here.
class SiteSetting(models.Model):
    favicon = models.ImageField(blank=True, null=True)
    header_logo = models.ImageField(blank=True, null=True)
    footer_logo = models.ImageField(blank=True, null=True)
    mobile_sale = models.CharField(max_length=20, blank=True, null=True)
    mobile_support = models.CharField(max_length=20, blank=True, null=True)
    email_sale = models.EmailField(blank=True, null=True)
    email_support = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=120, blank=True, null=True)

    office_hours = models.CharField(max_length=120, blank=True, null=True)

    facebook_url = models.URLField(default='https://', blank=True, null=True)
    linkedin_url = models.URLField(default='https://', blank=True, null=True)
    instagram_url = models.URLField(default='https://', blank=True, null=True)
    youtube_url = models.URLField(default='https://', blank=True, null=True)

