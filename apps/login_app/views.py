# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import User
# from ..rebelt_app.models import Quotes
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

# Create your views here.

def index(request):
    # User.objects.all().delete()
    return render(request, "login.html")

def register(request):
    results = User.objects.validate(request.POST)
    if results['status'] == True:
        user = User.objects.creator(request.POST)
        messages.success(request, 'User has been created.')
    else:
        for error in results['errors']:
            messages.error(request, error)
    return redirect("/")

def login(request):
    results = User.objects.loginVal(request.POST)
    if results['status'] == False:
        messages.error(request, "Please check your credentials, then try again.")
        return redirect('/')
    request.session['email'] = results['user'].email
    request.session['name'] = results['user'].name
    return redirect('/pokes')

def dashboard(request):
    if 'email' not in request.session:
        return redirect('/')
    return render(request, 'dashboard.html', { "quotes": Quotes.objects.all()})

def logout(request):
    request.session.flush()
    return redirect('/')

