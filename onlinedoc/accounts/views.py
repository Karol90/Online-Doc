from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response

def acc(request):
    user_tostring = User.objects.get(pk=1)
    #user_tostring = 'kurwa'
    return render_to_response('mainsite/inna.html', locals())