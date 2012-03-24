from accounts.models import Account
from django.contrib.auth.models import User
from django.http import HttpResponse

def index(request):
    u = User.objects.get(pk=1)
    output = 'user: ' + u.get_profile().to_string()
    return HttpResponse(output)