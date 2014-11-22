# -*- coding: utf-8 -*-
from django.http import HttpResponse
#from django.template.loader import get_template
#from django.template import Context
from django.shortcuts import render_to_response
import datetime

def home(request):
    current_date = datetime.datetime.now()
    #return HttpResponse("Welcome to the homepage!!")
    return render_to_response('home', locals())

def current_datetime(request):
    #now = datetime.datetime.now()
    current_date = datetime.datetime.now()
    #t = get_template('current_datetime')
    #html = t.render(Context({'current_date': now}))
    #html = "<html><body>时间It is now %s.</body></html>" % now
    #html = "时间It is now %s." % now
    #return HttpResponse(html)
    #return render_to_response('current_datetime', {'current_date': now})
    return render_to_response('current_datetime', locals())

def hours_ahead(request, offset):
    #try:
    #    offset = int(offset)
   # except ValueError:
    #    raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)


def hello(request):
    return HttpResponse("Hello World!!")
