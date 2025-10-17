from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
# Create your views here.
from django.views import View
from django.contrib import messages
from users.forms import SignupForm

from users.forms import LoginForm

from users.models import Customuser


class Home(View):
    def get(self,request):
        return render(request,'home.html')

class Register(View):
    def post(self,request):
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            u=form_instance.save(commit=False)
            u.is_active=False
            u.save()
            u.generate_otp()
            send_mail(
                "Django Auth OTP",
                u.otp,
                "arunbhaskaran85@gmail.com",
                [u.email],
                fail_silently=False,
            )
            return redirect('otp_verification')
        else:
            context={'form':form_instance}
            return render(request,'login.html',context)

    def get(self,request):
        form_instance=SignupForm()
        context={'form':form_instance}
        return render(request,'register.html',context)


class Otp_verification(View):
    def post(self,request):
        o=request.POST['o']
        try:
            u=Customuser.objects.get(otp=o)
            u.is_verified=True
            u.is_active=True
            u.save()
            return redirect('login')
        except:
            messages.error(request,'Invalid OTP')
            return render(request,'otp_verification.html')
    def get(self, request):
        return render(request,'otp_verification.html')


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