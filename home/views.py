from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from home.models import Task
# Create your views here.

def home(request):
 context = {'success' : False}
 if request.method == "POST":
  title = request.POST['title']
  desc = request.POST['desc']
  print(title,desc)
  ins = Task(taskTitle=title,taskDesc=desc)
  ins.save()
  context = {'success' : True}

 return render(request,'index.html',context)

def tasks(request):
 allTasks = Task.objects.all()

 context = {'tasks': allTasks}
 return render(request,'tasks.html',context)


def deletetasks(request,id):
  if request.method=="POST":
    di = Task.objects.get(pk=id)
    di.delete()
    return HttpResponseRedirect('/tasks') 

