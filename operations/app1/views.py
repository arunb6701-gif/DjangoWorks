from django.shortcuts import render

# Create your views here.
import math
def addition(request):
    if request.method=="POST":
        print(request.POST)
        n1=int(request.POST['n1'])
        n2=int(request.POST['n2'])
        s=n1+n2
        context={'result':s}
        return render(request,'addition.html',context)

    if request.method=="GET":
        return render(request,'addition.html')

def factorial(request):
    if request.method=="POST":
        print(request.POST)
        n1=int(request.POST['n1'])
        f=math.factorial(n1)
        context={'result':f}
        return render(request,'signupsignup.html',context)

    if request.method=="GET":
        return render(request,'signupsignup.html')



def bmi(request):

    if request.method=="POST":
        n1 = float(request.POST['n1'])
        n2 = float(request.POST['n2'])
        b=n2/n1**2
        context={'result':b}
        return render(request,'bmi.html',context)
    if request.method=="GET":
        return render(request,'bmi.html')
