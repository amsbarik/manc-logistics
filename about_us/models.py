from django.db import models


from core.models import BaseModel


# Create your models here.

class WorkingProcess(BaseModel):
    title = models.CharField(max_length=100)
    short_description = models.TextField(max_length=255)
    image = models.ImageField(upload_to='working_process/')
    order = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return self.title

    def clean(self):
        from django.core.exceptions import ValidationError

        if not self.pk and WorkingProcess.objects.count() >= 3:
            raise ValidationError("Maximum 3 working process steps are allowed.")
        


class ExpertTeam(BaseModel):
    name = models.CharField(max_length=120)
    designation = models.CharField(max_length=120)
    photo = models.ImageField(upload_to='expart_teams/')

    def __str__(self):
        return self.name