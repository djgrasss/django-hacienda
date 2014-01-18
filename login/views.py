# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate
from django.contrib.auth.views import login
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, HttpResponseRedirect

@csrf_protect
def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                return HttpResponseRedirect('/sdr/')
            else:
                c = {}
                c.update(csrf(request))
                c.update({'no_active':'Usuario inactivo'})
                return render_to_response('login/index.html', c)
        else:
            return login(request,template_name='login/index.html')
    return login(request, template_name='login/index.html')
