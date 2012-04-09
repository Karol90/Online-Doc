# coding=utf-8

from django.contrib.auth.models import User
from django.contrib.auth.views import auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.core.context_processors import csrf
from django.core.mail import send_mail

from onlinedoc.accounts.forms import LoginForm, RegisterForm
from onlinedoc.accounts.models import Account
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.template.loader import get_template
from django.template import Context
from django.core.mail.message import EmailMessage

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

def logout_view(request):
    logout(request)
    return redirect("/")

@login_required
def profile_view(request):
    print 'profile'
    user = request.user.get_profile()
    return render_to_response('accounts/profile.html', locals())

@csrf_exempt
def register_view(request):
    def errorHandle(error, account_form):
        return render_to_response("accounts/register.html", {
                                                             'error': error,
                                                             'account_form': account_form,
                                                             })
    if request.user.is_authenticated():
        return redirect('/')
    else:
        if request.method == 'POST':
            account_form = RegisterForm(request.POST)
            if account_form.is_valid():
                #try:
                    username = account_form.cleaned_data['username']
                    email = account_form.cleaned_data['email']
                    password = account_form.cleaned_data['password']
                    new_user = User.objects.create_user(username, email, password)
                    new_user.is_active = False  #wyłączenie konta
                    new_user.save()
                    
                    # Build the activation key for their account 
                    import datetime, random, sha                                                                                                                   
                    salt = sha.new(str(random.random())).hexdigest()[:5]
                    activation_key = sha.new(salt+new_user.username).hexdigest()
                    key_expires = datetime.datetime.today() + datetime.timedelta(2)
                    
                    account = account_form.save(commit=False)
                    account.user = new_user
                    account.activation_key = activation_key
                    account.key_expires = key_expires
                    account.save()
                    
                    # wysyłanie maila aktywacyjnego
                    email_subject = "Rejestracja w systemie OnlineDoc"
                    template = get_template('accounts/activation_mail.html')
                    body = template.render(Context({
                                             'link': 'http://'+request.META['HTTP_HOST']+'/accounts/activation/?activation_key='+activation_key
                                             }))
                    #send_mail(email_subject, body, 'rejestracja@onlinedoc.pl', [email])
                    
                    msg = EmailMessage(email_subject, body, 'rejestracja@onlinedoc.pl', [email])
                    msg.content_subtype = "html"  # Main content is now text/html
                    msg.send()
                    
                    return render_to_response("accounts/register_activation.html")
                #except:     #dodać obsługę błędów w różnych przypadkach
                   # error='Błąd zapisu'
                    #return errorHandle(error, account_form)
            else:
                error = u'form invalid'
                return errorHandle(error, account_form)
        else:
            account_form = RegisterForm()
            return render_to_response("accounts/register.html", {
                                                                 'account_form': account_form,
                                                                 })

def register_activation_view(request):
    activation_key = request.GET.get('activation_key')
    user_profile = get_object_or_404(Account,
                                     activation_key=activation_key)
    import datetime
    if user_profile.key_expires < datetime.datetime.today():
        return render_to_response('accounts/register_confirm.html', {'expired': True})
    user_account = user_profile.user
    user_account.is_active = True
    user_account.save()
    return render_to_response('accounts/register_confirm.html', {'success': True})
