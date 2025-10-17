
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#function based view

def Home(request):
    return HttpResponse('welcome to new django app')

# Index

def Index(request):
    return HttpResponse('index page')


