from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from django.views import View
from django.contrib import messages
from users.forms import SignupForm

from users.forms import LoginForm


class Home(View):
    def get(self,request):
        return render(request,'home.html')

class Register(View):
    def post(self,request):
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('login')
        else:
            context={'form':form_instance}
            return render(request,'login.html',context)

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
            if user and user.is_superuser==True:
                login(request, user)
                return redirect('adminhome')
            elif user and user.role=='student':
                login(request, user)
                return redirect('studenthome')
            elif user and user.role=='teacher':
                login(request, user)
                return redirect('teacherhome')
            else:
                messages.error(request,"invalid credentials")
                context={'form':form_instance}
                return render(request,'login.html',context)
    def get(self,request):
        form_instance=LoginForm()
        context={'form':form_instance}
        return render(request,'login.html',context)

class Userlogout(View):
    def get(self,request):
        logout(request)
        return redirect('login')

class Adminhome(View):
    def get(self,request):
        return render(request,'adminhome.html')

class Studenthome(View):
    def get(self,request):
        return render(request,'studenthome.html')

class Teacherhome(View):
    def get(self,request):
        return render(request,'teacherhome.html')