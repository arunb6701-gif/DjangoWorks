from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from users.forms import SignupForm,LoginForm


# Create your views here.

class Home(View):
    def get(self,request):
        return render(request,'home.html')

class Register(View):
    def post(self,request):
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('users:login')
        else:
            context={'form':form_instance}
            return render(request,'register.html',context)

    def get(self,request):
        form_instance=SignupForm()
        context={'form':form_instance}
        return render(request,'register.html',context)

class Userlogin(View):
    def post(self,request):
        form_instance=LoginForm(request.POST)
        if form_instance.is_valid():
            u=form_instance.cleaned_data['username']
            p=form_instance.cleaned_data['password']
            user=authenticate(username=u,password=p)
            if user:
                login(request,user)
                return redirect('users:home')
            else:
                messages.error(request,'invalid user credentials')
                context={'form':form_instance}
                return render(request,'login.html',context)


    def get(self,request):
        form_instance = LoginForm()
        context = {'form': form_instance}
        return render(request,'login.html',context)

class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('users:login')