from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render, redirect

import markdown
from re import sub
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate

def index(request):
    if not request.user.is_authenticated():
        return redirect('/users/login.html?next=%s' % request.path)
    #return render_to_response('website/index.html',
    #        context_instance=RequestContext(request)
    #        )


    return render(request, 'index.html', {"foo": "bar"})



