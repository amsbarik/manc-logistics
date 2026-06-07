from django.db import models


from core.models import BaseModel


# Create your models here.

class Service(BaseModel):
    title = models.CharField(max_length=100)
    short_description = models.TextField(max_length=100)
    thumbnail = models.ImageField(upload_to='services/')
    icon = models.ImageField(upload_to='icons/')

    def __str__(self):
        return self.title
