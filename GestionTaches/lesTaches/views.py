from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the lesTaches index.")
def home(request):
  return HttpResponse('bonjour à tous')
def home(request,name):
  return HttpResponse('bonjour depuis Django '+name)