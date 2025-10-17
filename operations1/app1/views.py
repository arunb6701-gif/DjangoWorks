from django.shortcuts import render

# Create your views here.
import math

from app1.forms import Additionform
from app1.forms import Bmi
from app1.forms import Signup,Calc

def addition(request):

    if request.method=='POST':
        print(request.POST)

        #create form instance using submitted data

        form_instance=Additionform(request.POST)

    #check whether the data is valid

        if form_instance.is_valid():

            #proccessing data

            data=form_instance.cleaned_data
            print(data)
            n1=data['num1']
            n2=data['num2']
            sum=int(n1)+int(n2)
            context={'result':sum,'form':form_instance}
            return render(request,'addition.html',context)

    if request.method=="GET":

        form_instance=Additionform()
        context={'form':form_instance}
        return render(request,'addition.html',context)



def signup(request):
    if request.method=="POST":
        print(request.POST)
        form_instance=Signup(request.POST)

        if form_instance.is_valid():
            data=form_instance.cleaned_data
            name=data['name']
            password=data['password']
            place=data['place']
            gender=data['gender']
            role=data['role']
            email=data['email']
            context={'name':name,'password':password,'place':place,'gender':gender,'role':role,'email':email,'form':form_instance}
            return render(request,'signup.html',context)

    if request.method=="GET":
        form_instance=Signup()
        context={'form':form_instance}
        return render(request,'signup.html',context)



def bmi(request):
        if request.method=="POST":
            print(request.POST)
            form_instance=Bmi(request.POST)
            if form_instance.is_valid():
                data=form_instance.cleaned_data
                h=data['weight']
                w=data['height']
                b=float(w)/float(h**2)
                context={'result':b,'form':form_instance}
                return render(request,'bmi.html',context)
        if request.method=="GET":
            form_instance=Bmi()
            context={'form':form_instance}
            return render(request,'bmi.html')


def calc(request):
    if request.method=="POST":
        form_instance=Calc(request.POST)

        if form_instance.is_valid():
            data=form_instance.cleaned_data
            print(data)
            w=int(data['weight'])
            h=int(data['height'])
            a=int(data['age'])
            g=data['gender']
            al=float(data['activity_levels'])
            print(w,h,a,g,al)

            if g=='male':
                bmr=10*w+6.25+h-5*a+5
            else:
                bmr=10*w+6.25+h-5*a-16.1
            c=bmr*al
            context={'result':c,'form':form_instance}
            return render(request,'calc.html',context)

    if request.method=="GET":
        form_instance=Calc()
        context={'form':form_instance}
        return render(request,'calc.html',context)

