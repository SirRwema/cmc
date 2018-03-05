from django.shortcuts import render
from django.http import Http404
from slider.models import RevSlider
from services.models import Service
from about.models import AboutIndex
from jobs.models import Jobs
from blog.models import BlogPost
from company_info.models import CompanyInfo


def index(request):
    slides = RevSlider.objects.all()
    slide1 = slides[0]
    slide2 = slides[1]
    slide3 = slides[2]
    services = Service.objects.all()
    about_us = AboutIndex.objects.all()
    jobs = Jobs.objects.all()
    blog_posts = BlogPost.objects.all()
    company_info = CompanyInfo.objects.all()
    company = company_info[0]

    return render(request, 'home/home.html',{
                'slide1':slide1,
                'slide2':slide2,
                'slide3':slide3,
                'services':services,
                'about_us':about_us,
                'jobs':jobs,
                'blog_posts':blog_posts,
                'company':company,
    })
