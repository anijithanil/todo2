from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import UpdateView,DeleteView

from .forms import Todoform
from .models import Todoapp

# Create your views here.
# def fun(request):
#     return render(request,'task_view.html')





def taskview(request):
    key = Todoapp.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        obj=Todoapp(name=name,priority=priority,date=date)
        obj.save()

    return render(request,'task_view.html',{'key':key})

def delete(request,id):
    obj=Todoapp.objects.get(id=id)
    if request.method=='POST':
        obj.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,pk):
    obj1=Todoapp.objects.get(id=pk)
    form=Todoform(request.POST or None,instance=obj1)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,})

