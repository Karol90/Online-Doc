from django.contrib.auth.models import User
from django.contrib.auth.views import auth_login
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf

from onlinedoc.accounts.forms import LoginForm
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth import authenticate, login

@login_required
def acc(request):
    user_tostring = User.objects.get(pk=1)
    return render_to_response('mainsite/inna.html', locals())

@csrf_exempt
def login_view(request):
    def errorHandle(error):
        form = LoginForm()
        return render_to_response('accounts/login.html', {
                'error' : error,
                'form' : form,
        })
    next = request.GET.get('next')
    if request.method == 'POST': # If the form has been submitted...
        print 'post'
        form = LoginForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            print 'form is valid'
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    print 'user is active'
                    # Redirect to a success page.
                    login(request, user)
                    return redirect('home')
                else:
                    # Return a 'disabled account' error message
                    error = u'account disabled'
                    return errorHandle(error)
            else:
                 # Return an 'invalid login' error message.
                error = u'invalid login'
                return errorHandle(error)
        else:
            error = u'form is invalid'
            return errorHandle(error)
    else:
        form = LoginForm() # An unbound form
        return render_to_response('accounts/login.html', {
            'form': form,
        })

def logout(request):
    print 'logout'
    return render_to_response('accounts/logout.html')

@login_required
def profile(request):
    print 'profile'
    user = request.user.get_profile()
    return render_to_response('accounts/profile.html', locals())

def register(request):
    print 'registration'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/books/")
    else:
        form = UserCreationForm()
    return render_to_response("accounts/register.html", {
        'form': form,
    })