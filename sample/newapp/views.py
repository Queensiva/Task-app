from django.shortcuts import render,redirect
from .models import Member


# Create your views here.
def index(request):
    mem = Member.objects.all()  # Fetch all Member objects
    return render(request,'index.html',{'mem':mem})

def add(request):
    return render(request,'add.html')

def addrec(request):
    x=request.POST['title']
    y=request.POST['description']
    z=request.POST['duedate']
    a=request.POST['priority']
    b=request.POST['status']
    mem=Member(title=x,description=y,duedate=z,priority=a,status=b)
    mem.save()
    return redirect("/")

def update(request,id):
    mem=Member.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})

def delete(request,id):
    mem=Member.objects.get(id=id)
    mem.delete()
    return redirect("/")

def uprec(request,id):
    x=request.POST['title']
    y=request.POST['description']
    z=request.POST['duedate']
    a=request.POST["priority"]
    b=request.POST["status"]
    mem=Member.objects.get(id=id)
    mem.title=x
    mem.description=y
    mem.duedate=z
    mem.priority=a
    mem.status=b
    mem.save()
    return redirect("/")


