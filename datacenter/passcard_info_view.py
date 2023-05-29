from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.visits_tools import get_duration
from datacenter.visits_tools import format_duration
from datacenter.visits_tools import is_visit_long
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    this_passcard_visits = []
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    for visit in visits:
        duration = get_duration(visit)
        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at.strftime("%d %B %Y %H:%M"),
                'duration': format_duration(duration),
                'is_strange': is_visit_long(duration)
            }
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
