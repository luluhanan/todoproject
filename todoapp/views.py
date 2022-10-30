

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, DetailView, UpdateView
from .forms import TaskForm
from .models import Task
# Create your views here.

class Tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'list'

class Taskdetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'

class Taskupdateview(UpdateView):
        model = Task
        template_name = 'update.html'
        context_object_name = 'task'
        fields = ('name','priority','date')

        def get_success_url(self):
            return reverse_lazy('detailview',kwargs={'pk':self.object.id})

class Taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('listview')


def home(request):
    list = Task.objects.all()
    if request.method == 'POST':
        name=request.POST.get('task')
        priority=request.POST.get('priority')
        date = request.POST.get('date')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'list':list})

def delete(request,id):
    task=Task.objects.get(id=id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    form=TaskForm(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'task':task,'form':form})