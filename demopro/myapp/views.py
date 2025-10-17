from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# def First(request):
#     return HttpResponse('first page')
#
# def Second(request):
#     return HttpResponse('second page')

def first(request):
    context={'name':'arun','age':23}
    return render(request,'first.html',context)
def second(request):
    context={'name':'abhi','place':'ekm'}
    return render(request,'second.html',context)