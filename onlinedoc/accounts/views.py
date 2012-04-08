from django.contrib.auth.models import User
from django.contrib.auth.views import auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf

from onlinedoc.accounts.forms import LoginForm, RegisterForm
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth import authenticate, login

@login_required
def acc(request):
    user_tostring = User.objects.get(pk=1)
    return render_to_response('mainsite/inna.html', locals())

@csrf_exempt
def login_view(request):
    def errorHandle(error, form):
        #form = LoginForm()
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
                    error = u'account disabled'
                    return errorHandle(error, form)
            else:
                 # Return an 'invalid login' error message.
                error = u'invalid login'
                return errorHandle(error, form)
        else:
            error = u'form is invalid'
            return errorHandle(error, form)
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

@csrf_exempt
def register(request):
    def errorHandle(error, user_form, account_form):
        return render_to_response("accounts/register.html", {
                                                             'error': error,
                                                             'user_form': user_form,
                                                             'account_form': account_form,
                                                             })
    
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        account_form = RegisterForm(request.POST)
        if user_form.is_valid() and account_form.is_valid():
            new_user = user_form.save()
            account = account_form.save(commit=False)
            account.user = new_user
            account.save()
            return render_to_response("accounts/register_activation.html")
        else:
            error = u'form invalid'
            return errorHandle(error, user_form, account_form)
    else:
        user_form = UserCreationForm()
        account_form = RegisterForm()
        return render_to_response("accounts/register.html", {
                                                             'user_form': user_form,
                                                             'account_form': account_form,
                                                             })


