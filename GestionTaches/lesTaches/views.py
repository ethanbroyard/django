from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from lesTaches.models import Task

def index(request):
    return HttpResponse("Hello, world. You're at the lesTaches index.")
def home(request):
  return HttpResponse('bonjour à tous')
def home(request,name):
  return HttpResponse('bonjour depuis Django '+name)

def task_listing(request):
  tasks = Task.objects.all().order_by('due_date')
  return render(request,template_name='lesTaches/list2.html',context={'objects':tasks})

def task_listing2(request):
  objets = Task.objects.all().order_by('-due_date')
  # - (inverse l'ordre )
  return render(request,template_name='lesTaches/list.html', context={'taches':objets})

def details(request,tache_id):
  task = get_object_or_404(Task, pk=tache_id)
  return render(request,template_name='lesTaches/details.html',context={'tache':task})