from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    h1 = "kupa"
    return render_to_response('mainsite/index.html', locals())
