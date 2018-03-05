from django.shortcuts import render
from django.http import Http404

from jobs.models import Jobs, JobIndex


def JobsPage(request):
    jobs = Jobs.objects.all()
    return render(request, 'jobs/jobs.html',{
                'jobs':jobs,
    })

def Job_Details(request, id):
    try:
        job = Jobs.objects.get(id=id)
    except Jobs.DoesNotExist:
        raise Http404('This job does not exist')
    return render(request, 'jobs/job_details.html',{
        'job':job,
    })
