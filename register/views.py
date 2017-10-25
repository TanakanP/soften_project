# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import SignUpForm
from django.http import HttpResponse


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.address = form.cleaned_data.get('address')
            user.profile.phone = '+66'
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
        return HttpResponse(status=204)
    else:
        form = SignUpForm()
    return HttpResponse(status=204)


def log(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
    else:
        return HttpResponse(status=204)
