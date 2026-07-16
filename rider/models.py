from django.db import models

from core.models import BaseModel



class RiderRecruitment(BaseModel):

    heading = models.CharField(max_length=200)
    short_description = models.TextField()
    thumbnail = models.ImageField(upload_to="thumbnails/")

    with_car_txt = models.TextField()
    without_car_txt = models.TextField()

    def __str__(self):
        return self.heading

