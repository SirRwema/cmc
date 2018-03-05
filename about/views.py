from django.shortcuts import render
from django.http import Http404
from about.models import AboutUs,AboutIndex,CompanyHistory



def AboutPage(request):
    about_co = AboutUs.objects.order_by('id')[0]
    co_history = CompanyHistory.objects.all()
    about_us = AboutIndex.objects.all()
    about = about_us[0]
    return render(request, 'about/about.html',{
                'about_us':about_us,
                'about':about,
                'about_co':about_co,
                'co_history':co_history
    })
