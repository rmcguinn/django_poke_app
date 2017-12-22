# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Poke
from ..login_app.models import *
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from datetime import date

# Create your views here.

def pokes(request):
    welcome = request.session['name']
    print (request.session['name'])
    return render(request, "dashboard.html", {"welcome": request.session['name'], "users": User.objects.all().exclude(name=request.session['name'])})



def button(request):
    return redirect("/pokes")

