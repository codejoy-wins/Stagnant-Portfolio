# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index (request):
    return render(request, 'index.html')

def process(request):
    print "processing"
    request.session['first'] = request.POST['first']
    request.session['second'] = request.POST['second']
    request.session['third'] = request.POST['third']
    request.session['fourth'] = request.POST['fourth']
    request.session['fifth'] = request.POST['fifth']
    request.session['sixth'] = request.POST['sixth']
    request.session['xp'] = request.POST['xp']
    listx = []
    listx.append(request.POST['first'])
    listx.append(request.POST['second'])
    listx.append(request.POST['xp'])

    request.session['listx'] = listx
    print listx
    return redirect("/")

def another(request):
    print "another"
    return render(request, 'another.html')

def odell (request):
    return render(request, 'odell.html')
