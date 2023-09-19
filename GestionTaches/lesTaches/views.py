from django.forms import ModelForm, Textarea
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from lesTaches.models import Task
from django.contrib import messages

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

class TaskForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Nom "
        self.fields['description'].label = "description"
       
    class Meta:
        model = Task
        fields = ('name', 'description')
        widgets = {'description': Textarea(attrs={'cols': 60, 'rows': 10}),}
    
def ajout(request):
        objets = Task.objects.all().order_by('-due_date')
        form = TaskForm()
        if request.method == "POST":
            form = TaskForm(request.POST)
            if form.is_valid():
                new_task = form.save()
                messages.success(request,'Nouvelle tache '+new_task.name+' '+new_task.description)
                context = {'pers': new_task}
                
                return render(request,template_name='lesTaches/list2.html', context={'objects':objets})
        context = {'form': form}
        return render(request,template_name='lesTaches/ajout.html', context={'form':form})
    