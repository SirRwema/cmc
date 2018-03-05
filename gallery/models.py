from django.db import models
from django.template.defaultfilters import slugify

class GalleryName(models.Model):
    name = models.CharField(max_length = 100, null=False,blank=True)

def get_image_filename(instance, filename):
    name = instance.gallery_name.name
    slug = slugify(name)
    return "media/gallery_images/%s-%s" % (slug, filename)   
class ImageGallery(models.Model):
    gallery_name = models.ForeignKey(GalleryName, default=None, on_delete=models.PROTECT)
    gallery_pics = models.ImageField(upload_to = get_image_filename,verbose_name='Gallery-Image')
