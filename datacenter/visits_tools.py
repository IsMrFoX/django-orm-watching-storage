from datetime import timedelta
from django.utils import timezone


def is_visit_long(duration, minutes=60):
    return duration > timedelta(minutes=minutes)


def get_duration(visit):
    entered_at_local = timezone.localtime(visit.entered_at)
    leaved_at = timezone.localtime(visit.leaved_at)
    duration = leaved_at - entered_at_local
    return duration


def format_duration(duration):
    hours = duration.seconds // 3600
    minutes = (duration.seconds % 3600) // 60
    if duration.days:
        return f"{duration.days} {hours:02}:{minutes:02}"
    return f"{hours:02}:{minutes:02}"
