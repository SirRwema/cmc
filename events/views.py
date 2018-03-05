from django.shortcuts import render
from django.http import Http404

from events.models import Events, EventsIndex


def EventsPage(request):
    events = Events.objects.all()
    events_banner = EventsIndex.objects.order_by('id')[0]
    return render(request, 'events/events.html',{
                'events':events,
                'events_banner':events_banner,
    })

def Event_Details(request, id):
    try:
        event = Events.objects.get(id=id)
    except Events.DoesNotExist:
        raise Http404('This event does not exist')
    return render(request, 'events/event_details.html',{
        'event':event,
    })
