from django.db import models

class RevSlider(models.Model):
    title =  models.CharField(max_length=200, null=False,blank=False,default=None)
    sub_text =  models.CharField(max_length=800, null=False,blank=False,default=None)
    button_text = models.CharField(max_length=100, null=False,blank=False, default=None)
    slider_image = models.ImageField(upload_to = 'media/images/slider/', default =None)

