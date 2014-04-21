from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render, redirect

from django.core import serializers

from django.http import HttpResponseRedirect
import sys, traceback

from DNDSync.models import *

def index(request):
    if not request.user.is_authenticated():
        return redirect('/users/login.html?next=%s' % request.path)



    char = Character.objects.get( charName=request.user.username )
    notes = char.notes
    journal = char.journal
    
    page_info = {
        "character": char,
        "notes":notes,
        "journal":journal,

        }

    return render(request, 'index.html', page_info)



def updateValues(request):
    print "\n\nupdateValues:"
    print request.POST
    print '\n'.join([ "%s: %s"%(k,v) for k,v in request.POST.items() ])
    char = Character.objects.get( charName=request.user.username )
    print "Got charName:",char.charName
    key = request.POST['id'].lower().rstrip()
    val = request.POST['value']
    print "Using:",key,val
    try:

        if 'journal' in key:
            print "Key was journal"
            char.journal.add(value=val)
            print "Added new journal entry"
            char.save()
            print "Saved character"
            return HttpResponse( char.journal.all() )
        
        if 'notes' in key:
            print "notes was in key"
            note = Notes(value=val)
            print "Saving note"
            note.save()
            print "Made new note!"
            char.notes.add(note)
            print "Got character:",char.charName
            char.save()
            print "Saved character"
            return HttpResponse( char.notes.all() )
        
        else:
            print "Getting oldVal from",char.charName
            oldVal = getattr(char,key)
            print "Was: ",oldVal
            setattr(char,key,val)
            newVal = getattr(char,key)
            print "Now: ",newVal
            char.save()
            return HttpResponse(newVal)

    except ValueError:
        #traceback.print_exc(file=sys.stdout)
        print "\n***ValueError***\n"
        return HttpResponse( -1 )
    print "\n\n"
    return HttpResponse(newVal)
