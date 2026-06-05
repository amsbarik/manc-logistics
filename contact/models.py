from django.db import models

# Create your models here.
# # ///////////////////////////////////

# class Contact(CoreModel):
#     user_name = models.CharField(max_length=100)
#     user_mobile = models.CharField(max_length=15, null=True)
#     user_email = models.EmailField(blank=True)
#     user_message = models.TextField()
    
#     location_map_url = models.URLField(default="https://")
    
#     STATUS_CHOICES = [
#         ('un_read', 'Un-read'),
#         ('read', 'Read'),
#         ('contact', 'Contacted'),
#         ('on_hold', 'On Hold'),
#         ('follow_up', 'Follow-up'),
#         ('confirm', 'Confirm'),
#         ('cancelled', 'Cancelled'),
#     ]
    
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='un_read')
#     remark = models.TextField(default='', blank=True)

#     def change_status(self, new_status):
#         if new_status in dict(self.STATUS_CHOICES):
#             self.status = new_status
#             self.save()
            
#     def __str__(self):
#         return self.name
    

