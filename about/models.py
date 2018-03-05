import datetime
from django.db import models


class AboutUs(models.Model):
    title = models.CharField(max_length=100,null=False,blank=False)
    section = models.CharField(max_length=300,null=False,blank=False)
    aboutus_image = models.ImageField(upload_to = 'media/images/services/', default = 'pic_folder/None/no-img.jpg')
    aboutus_description = models.TextField()

class AboutIndex(models.Model):
    frontpage_title = models.CharField(max_length=100,null=False,blank=False, default="About us front page title")
    sub_text = models.CharField(max_length=400,null=False,blank=False,default="About us front page sub-text")
    video_intro = models.CharField(max_length=200, null=False, blank=False, default="Watch Intro Video<br>About Us")
    about_banner = models.ImageField(upload_to = 'media/images/banners/', default = 'pic_folder/None/no-img.jpg')

class CompanyHistory(models.Model):
    YEAR_CHOICES = [(r,r) for r in range(1984, datetime.date.today().year+1)]
    history_title = models.CharField(max_length=100,null=False,blank=False)
    history_description = models.TextField(default="Tell us your history")
    year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    