from django.shortcuts import render, redirect

from app1.forms import Movieform
from app1.models import Moviedetail

# Create your views here.

def movielist(request):
        b =Moviedetail.objects.all()  # to read all record from table
        context = {'Moviedetail': b}
        return render(request,'movielist.html',context)

def addmovie(request):
    if request.method=="POST": #after submission
        form_instance=Movieform(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            context={'form':form_instance}
            return render(request,'addmovie.html',context)

    if request.method=="GET":
        form_instance=Movieform()
        context={'form':form_instance}
        return  render(request,'addmovie.html',context)

def moviedetails(request,i):
    if request.method=="GET":
        b=Moviedetail.objects.get(id=i)
        context={'movie':b}
        return render(request,'moviedetails.html',context)

def update(request,i):
    if request.method=="POST":
        b=Moviedetail.objects.get(id=i)
        form_instance=Movieform(request.POST,request.FILES,instance=b)
        if form_instance.is_valid():
            form_instance.save()
            redirect('app1:movielist')

    if request.method=="GET":
        b=Moviedetail.objects.get(id=i)
        form_instance=Movieform(instance=b)
        context={'movie':form_instance}
        return render(request,'update.html',context)

def delete(request,i):
    b=Moviedetail.objects.get(id=i)
    b.delete()
    return redirect('app1:movielist')

