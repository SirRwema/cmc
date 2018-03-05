import datetime
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100,null=False,blank=False)
    sub_title = models.CharField(max_length=300,null=False,blank=False)
    description = models.TextField()
    date_added = models.DateField(("Date Added"), default=datetime.date.today)
    blog_image = models.ImageField(("Featured image"),upload_to = 'media/images/blogposts/', default = 'pic_folder/None/no-img.jpg')

class BlogIndex(models.Model):
    blog_banner = models.ImageField(("Page Banner"),upload_to = 'media/images/banners/', default = 'pic_folder/None/no-img.jpg')

