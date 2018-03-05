import datetime
from django.db import models

class Events(models.Model):
    title = models.CharField(max_length=500, null=False, blank=False)
    sub_title = models.CharField(max_length=1000, null=False, blank=False)
    start_time = models.TimeField(("Start Time"), default=datetime.time())
    end_time = models.TimeField(("End Time"), default=datetime.time())
    start_date =models.DateField(("Start Date"), default=datetime.date.today)
    end_date = models.DateField(("End Date"), default=datetime.date.today)
    location = models.CharField(max_length=100, null=False, blank=False)
    events_image = models.ImageField(upload_to = 'media/images/events/', default = 'pic_folder/None/no-img.jpg')
    description = models.TextField()

class EventsIndex(models.Model):
    events_banner = models.ImageField(upload_to = 'media/images/banners/', default = 'pic_folder/None/no-img.jpg')
