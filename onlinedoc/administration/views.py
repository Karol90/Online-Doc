from administration.models import UserProfile
from django.contrib.auth.models import User
from django.http import HttpResponse

def index(request):
    u = User.objects.get(pk=1)
    output = 'user: '+u.get_profile().firstname
    return HttpResponse(output)