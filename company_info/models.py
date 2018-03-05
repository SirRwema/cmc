import datetime
from django.db import models

class CompanyInfo(models.Model):
    co_name = models.CharField(max_length=100,null=False,blank=False)
    co_industry = models.CharField(max_length=300,null=False,blank=False)
    co_address = models.CharField(max_length=300,null=False,blank=False)
    co_address_2 = models.CharField(max_length=300,null=False,blank=False)
    office_longitude = models.DecimalField(max_digits=20, decimal_places=10,null=False,blank=False)
    office_latitude = models.DecimalField(max_digits=20, decimal_places=10,null=False,blank=False)
    co_email = models.EmailField(null=False, blank=False)
    phone_number = models.CharField(max_length=15)
    phone_number2 = models.CharField(max_length=15)
    fax_number = models.CharField(max_length=15)        
    co_description = models.TextField()
    co_PC_logo = models.ImageField(upload_to = 'media/images/logos/', default = 'pic_folder/None/no-img.jpg')
    co_Phone_logo = models.ImageField(upload_to = 'media/images/logos/', default = 'pic_folder/None/no-img.jpg')
    co_Retina_logo = models.ImageField(upload_to = 'media/images/logos/', default = 'pic_folder/None/no-img.jpg')

