# coding=utf-8

from visits_calendar import VisitsCalendar
from django.template.loader_tags import register
from django.utils.safestring import mark_safe

from onlinedoc.accounts.models import Doctor

@register.inclusion_tag('worktimes/calendar.html')
def render_monthly_calendar(year, month, doctor):
  if doctor=='None':
      doctor = Doctor.objects.all()[:1]
  
  cal = VisitsCalendar(doctor).formatmonth(year, month)
  return {'calendar': mark_safe(cal)}