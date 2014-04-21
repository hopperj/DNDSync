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

from DNDSync.models import *

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
                character = Character.objects.create(charName=charName)
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

        char = Character.objects.get( charName=user.username )
        print char.charName
        return HttpResponseRedirect(redirect_to or '/')

    print user
    print("There is a problem with your username or password.")
    return render_to_response('login.html',
                              {'loginError':"There is a problem with your username or password."},
                              context_instance=RequestContext(request)
                              )

