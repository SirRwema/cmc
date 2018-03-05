from django.shortcuts import render
from django.http import Http404
from gallery.models import GalleryName, ImageGallery



def GalleryPage(request):
    gallery_images = ImageGallery.objects.all()
    return render(request, 'gallery/gallery.html',{
                'gallery_images':gallery_images,
    })


