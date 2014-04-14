from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render#render_to_response, get_object_or_404, redirect

import markdown
from re import sub
from django.http import HttpResponseRedirect



def index(request):

    #return render_to_response('website/index.html',
    #        context_instance=RequestContext(request)
    #        )


    return render(request, 'index.html', {"foo": "bar"})# 'website/index.html'




