"""cmc_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from slider.views import index
from about.views import AboutPage
from services.views import ServicesPage,Service_Details
from jobs.views import JobsPage,Job_Details
from events.views import EventsPage, Event_Details
from gallery.views import GalleryPage
from blog.views import BlogPage,Blog_Details

urlpatterns = [
    url(r'^$', index, name='index'),   
    path('about/', AboutPage, name = 'about_page'),
    path('services/', ServicesPage, name = 'services_page'),   
    path('services/<id>/', Service_Details, name='service_details'),
    path('jobs/',JobsPage, name='jobs_page'),
    path('jobs/<id>', Job_Details, name='job_details'),
    path('events/',EventsPage, name='events_page'),
    path('events/<id>/', Event_Details, name='event_details'),
    path('gallery/', GalleryPage, name='gallery_page'),
    path('blog/', BlogPage, name='blog_page'),
    path('blog/<id>/',Blog_Details, name='blog_details'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
