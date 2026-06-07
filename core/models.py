from django.db import models

# Create your models here.



# base model
class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["order", "-created_at"]



# HeroSlider model
class HeroSlider(BaseModel):
    heading = models.CharField(max_length=200, blank=True)
    short_description = models.TextField(blank=True)
    image = models.ImageField(upload_to='heor_slider_img/')

    cta_message = models.CharField(max_length=100, blank=True)
    primary_btn_txt = models.CharField(max_length=100, blank=True)
    primary_btn_url = models.URLField(max_length=250, blank=True)

    secondary_btn_txt = models.CharField(max_length=100, blank=True)
    secondary_btn_url = models.URLField(max_length=250, blank=True)


    def __str__(self):
        return self.heading


# Partner model
class Partner(BaseModel):
    name = models.CharField(max_length=120)
    partner_logo = models.ImageField(upload_to='partners/')

    def __str__(self):
        return self.name
    

#  message from model 
class LeadershipMessage(BaseModel):
    heading = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="leadership/")
    message_01 = models.TextField()
    message_02 = models.TextField(blank=True)

    def __str__(self):
        return self.name
        

# WhyChooseUs model 
class WhyChooseUs(BaseModel):
    icon = models.ImageField(upload_to='icons/')
    title = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.title
    


# FAQ
class FAQ(BaseModel):

    class FAQType(models.TextChoices):
        RIDER = "RIDER", "Rider"
        MERCHANT = "MERCHANT", "Merchant"

    question = models.CharField(max_length=255)
    answer = models.TextField()
    faq_type = models.CharField(max_length=20, choices=FAQType.choices, default=FAQType.RIDER)

    def __str__(self):
        return self.question
    




# Newsletter model
class Newsletter(BaseModel):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
    



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
    about_company = models.TextField()

    facebook_url = models.URLField(default='https://', blank=True, null=True)
    linkedin_url = models.URLField(default='https://', blank=True, null=True)
    instagram_url = models.URLField(default='https://', blank=True, null=True)
    tiktok_url = models.URLField(default='https://', blank=True, null=True)
    youtube_url = models.URLField(default='https://', blank=True, null=True)

    meta_title = models.CharField(max_length=255, blank=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.TextField(blank=True, help_text='Separate keywords with commas (,).')
    og_image = models.ImageField(upload_to="seo/", blank=True, null=True)
    google_site_verification = models.CharField(max_length=255, blank=True)





# # Home Page Banners 
# class Banner(CoreModel):
#     top_banner = models.ImageField(blank=True, null=True)
#     top_banner_url = models.URLField(blank=True, null=True, default="https://")
    
#     banner_ads1 = models.ImageField(blank=True, null=True)
#     banner_ads2 = models.ImageField(blank=True, null=True)
#     banner_ads3 = models.ImageField(blank=True, null=True)
#     banner_ads4 = models.ImageField(blank=True, null=True)










