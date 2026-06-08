from django.db import models


from core.models import BaseModel


# Create your models here.

# About Section
class About(BaseModel):
    heading = models.CharField(max_length=150)
    short_description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/')

    mission = models.TextField()
    vision = models.TextField()

    mission_icon = models.ImageField(upload_to='icons/', blank=True)
    vision_icon = models.ImageField(upload_to='icons/', blank=True)

    feature_01 = models.CharField(max_length=200, blank=True)
    feature_02 = models.CharField(max_length=200, blank=True)
    feature_03 = models.CharField(max_length=200, blank=True)
    feature_04 = models.CharField(max_length=200, blank=True)
    feature_05 = models.CharField(max_length=200, blank=True)
    feature_06 = models.CharField(max_length=200, blank=True)
    feature_07 = models.CharField(max_length=200, blank=True)

    def clean(self):
        from django.core.exceptions import ValidationError

        if not self.pk and About.objects.exists():
            raise ValidationError(
                "Only one About section is allowed."
            )

    def __str__(self):
        return self.heading
    


# About Features
# class AboutFeature(BaseModel):
#     about = models.ForeignKey( About, on_delete=models.CASCADE, related_name='features')
#     feature = models.CharField(max_length=200)

#     def __str__(self):
#         return self.feature

#     class Meta:
#         ordering = ['order']




# Working Process 
class WorkingProcess(BaseModel):
    title = models.CharField(max_length=100)
    short_description = models.TextField(max_length=255)
    image = models.ImageField(upload_to='working_process/')

    def __str__(self):
        return self.title

    def clean(self):
        from django.core.exceptions import ValidationError

        if not self.pk and WorkingProcess.objects.count() >= 3:
            raise ValidationError("Maximum 3 working process steps are allowed.")
        


# Expert Team
class ExpertTeam(BaseModel):
    name = models.CharField(max_length=120)
    designation = models.CharField(max_length=120)
    photo = models.ImageField(upload_to='expart_teams/')

    def __str__(self):
        return self.name