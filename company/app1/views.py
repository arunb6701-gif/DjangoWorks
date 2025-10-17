from django.shortcuts import render, redirect

from app1.forms import Employeeform

from app1.forms import Employee

# Create your views here.

def home(request):
    return render(request,'home.html')

def addemployee(request):
    if request.method=="POST":
        print(request.POST)
        print(request.FILES)
        form_instance=Employeeform(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('app1:viewemployee')

    if request.method=="GET":
        form_instance=Employeeform()
        context={'form':form_instance}
        return render(request,'addemp.html',context)

def viewemployee(request):
    v=Employee.objects.all()
    context={'form':v}
    return render(request,'viewemp.html',context)