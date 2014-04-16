# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.core.context_processors import csrf
from django.core.urlresolvers import reverse

from django.db import IntegrityError

def index(request):
    return render_to_response('index.html',
            page_info,            
            context_instance=RequestContext(request)
            )

def user_registration(request):
    if request.POST:
        print "Processing new user form"
        charName = request.POST.get('charName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        next_page = request.POST.get('next')
        try:
            print "Testing authenticate"
            if authenticate(username=charName, password=password) is None:
                user = User.objects.create_user(username=charName, email=email, password=password)
                user.save()
                print "User saved"
            else:
                print "Must have been another user"
                return render_to_response('registration.html',
                                          {'regError':'An account with this information exists already'},
                                          context_instance=RequestContext(request)
                                          )
        except IntegrityError:
            print "Integrity Error"
            return render_to_response('registration.html',
                                      {'regError':'An account with this information exists already'},
                                  context_instance=RequestContext(request)
                                  )

        user = authenticate(username=charName, password=password)
        if user is not None:
            print "Logging in"
            login(request, user)
            return HttpResponseRedirect('/')

        print "Going back to registration page"
    return render_to_response('registration.html',
                              context_instance=RequestContext(request)
                              )


def user_logout(request):    
    redirect_to = request.REQUEST.get('next', '')
    logout(request)
    return HttpResponseRedirect(redirect_to or '/')


    
def user_login(request):
    if not request.POST:
        return render_to_response('login.html',
                                  context_instance=RequestContext(request)
                                  )

    username = request.POST.get('username')
    password = request.POST.get('password')
    redirect_to = request.REQUEST.get('next', '')
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        print("User is valid, active and authenticated")
        return HttpResponseRedirect(redirect_to or '/')

    print user
    print("There is a problem with your username or password.")
    return render_to_response('login.html',
                              {'loginError':"There is a problem with your username or password."},
                              context_instance=RequestContext(request)
                              )


def user_login_old(request):
    state = "Please log in below..."
    username = password = ''
    redirect_to = request.REQUEST.get('next', '')
    login_error = '0'
    print 'redirect_to:',redirect_to
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_page = request.POST.get('next')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                django.contrib.auth.login(request, user)
                if len(redirect_to) > 1: 
                    return HttpResponseRedirect(redirect_to)
                else:
                    print "REDIRECT TO WAS EMPTY:",redirect_to
                    return HttpResponseRedirect(reverse('websiteIndex'))
                state = "You're successfully logged in!"
            else:
                print "\n\n","Error: Could not verify login/password"
                login_error = '1'
                state = "Your account is not active, please contact the site admin."
        else:
            print "\n\n","Error: Could not verify login/password"
            login_error = '1'
            state = "Your username and/or password were incorrect."
    page_info = {
        "login_error":login_error,
        "state":state,
        "username":username,
        }
    page_info.update( {"next":redirect_to,} )

    return render_to_response('login.html',
            page_info,    
            context_instance=RequestContext(request)
            )
    

def user_registration_old(request):
    state = "Please log in below..."
    username = password = charName = ''
    redirect_to = request.REQUEST.get('next', '')
    login_error = '0'
    print 'redirect_to:',redirect_to
    if request.POST:
        username = request.POST.get('username')
        charName = request.POST.get('charName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        next_page = request.POST.get('next')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                django.contrib.auth.login(request, user)
                if len(redirect_to) > 1: 
                    return HttpResponseRedirect(redirect_to)
                else:
                    print "REDIRECT TO WAS EMPTY:",redirect_to
                    return HttpResponseRedirect(reverse('main_index'))
                state = "You're successfully logged in!"
            else:
                print "\n\n","Error: Could not verify login/password"
                login_error = '1'
                state = "Your account is not active, please contact the site admin."
        else:
            print "\n\n","Creating new user....."
            user = User.objects.create_user(username, charName, email, password)
            print "User was created:",request.user.is_authenticated()
    page_info = {
        "login_error":login_error,
        "state":state,
        "username":username,
        }
    page_info.update(csrf(request))

    page_info.update( {"next":redirect_to,} )

    return render_to_response('registration.html',
            page_info,    
            context_instance=RequestContext(request)
            )
