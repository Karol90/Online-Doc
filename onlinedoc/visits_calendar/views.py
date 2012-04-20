# coding=utf-8

#z projektu
from visits_calendar import VisitsCalendar
from onlinedoc.accounts.models import Doctor

from django.template.loader_tags import register
from django.utils.safestring import mark_safe
from django.shortcuts import render_to_response
from django.template.context import RequestContext


def monthly_calendar(request):
    import datetime
    now = datetime.datetime.now()
    cal = VisitsCalendar(None).formatmonth(now.year, now.month)
    return render_to_response('visits_calendar/monthly.html', {'calendar': mark_safe(cal)}, context_instance=RequestContext(request))


#partial view
@register.inclusion_tag('visits_calendar/render_monthly.html')
def render_monthly_calendar(year, month, doctor):
  
  cal = VisitsCalendar(doctor).formatmonth(year, month)
  return {'calendar': mark_safe(cal)} #ciekawe co robi mark_safe...?