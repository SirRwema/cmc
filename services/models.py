from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    services_icon = models.CharField(max_length=100, default="ion-clipboard")
    services_image = models.ImageField(upload_to = 'media/images/services/', default = 'pic_folder/None/no-img.jpg')

class ServiceIndex(models.Model):
    service_banner = models.ImageField(upload_to = 'media/images/banners/', default = 'pic_folder/None/no-img.jpg')