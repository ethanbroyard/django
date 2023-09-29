from django.forms import ModelForm, Textarea, Form
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.urls import reverse
from lesTaches.models import Task
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView


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

 
# def ajout(request):
#         objets = Task.objects.all().order_by('-due_date')
#         form = TaskForm()
        
#         if request.method == "POST":
#             form = TaskForm(request.POST)
#             if form.is_valid():
#                 new_task = form.save()
#                 messages.success(request,'Nouvelle tache '+new_task.name+' '+new_task.description)
#                 context = {'tache': new_task}
                
#                 return render(request,template_name='lesTaches/list2.html', context={'objects':objets})
#         context = {'form': form}
#         return render(request,template_name='lesTaches/Task_form.html', context={'form':form})
  


class TaskCreate(CreateView):
  model=Task
  fields = ['name', 'description']
  initial = {'name': 'test a changer'}
  success_url="/lesTaches/taches/"

class TaskUpdate(UpdateView):
  model = Task
  fields = '__all__' # Non recommandé (problème potentiel de sécurité si on ajoute d'autres champs)
  success_url="/lesTaches/taches/"
  
class TaskDelete(DeleteView):
  model = Task
  success_url = "/lesTaches/taches/"

# https://developer.mozilla.org/fr/docs/Learn/Server-side/Django/Forms#vues_g%C3%A9n%C3%A9riques_d%C3%A9dition