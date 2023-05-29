from datacenter.models import Visit
from django.shortcuts import render
from datacenter.visits_tools import get_duration
from datacenter.visits_tools import format_duration
from django.utils import timezone


def storage_information_view(request):
    non_closed_visits = []
    visits = Visit.objects.filter(leaved_at__isnull=True)
    for visit in visits:
        duration = get_duration(visit)
        non_closed_visits.append(
            {
                'who_entered': visit.passcard,
                'entered_at': timezone.localtime(visit.entered_at).strftime('%Y-%m-%d %H:%M'),
                'duration': format_duration(duration),
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
