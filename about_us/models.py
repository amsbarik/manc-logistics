from django.db import models


from core.models import BaseModel

# Create your models here.



class ExpertTeam(BaseModel):
    name = models.CharField(max_length=120)
    designation = models.CharField(max_length=120)
    photo = models.ImageField(upload_to='expart_teams/')

    def __str__(self):
        return self.name