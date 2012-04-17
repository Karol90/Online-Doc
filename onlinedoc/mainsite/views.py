from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.template.loader_tags import register

from onlinedoc.worktimes.views import render_monthly_calendar

def index(request):
    return render_to_response('mainsite/index.html', context_instance=RequestContext(request))