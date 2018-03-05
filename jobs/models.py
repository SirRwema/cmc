import datetime
from django.db import models

class Jobs(models.Model):
    CATEGORY_CHOICES = [("Information Technology","Information Technology"),("Bio-Technology","Bio-Technology"),("Teaching","Teaching"),("Medicine","Medicine"),("Other","Other")]
    title = models.CharField(max_length=200)
    category = models.CharField(('Job Category'),max_length=200, choices=CATEGORY_CHOICES, default="Other")
    description = models.TextField()
    job_icon = models.CharField(max_length=100, null=False, blank=False)
    Expiry_date = models.DateField(("Expiry Date"), default=datetime.date.today)

class JobIndex(models.Model):
    job_banner = models.ImageField(upload_to = 'images/banners/', default = 'pic_folder/None/no-img.jpg')
