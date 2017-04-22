# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    context['name'] = 'Joey'
    return render(request, 'test.html', context)

def test(request):
    return HttpResponse("Hello world ! ")
