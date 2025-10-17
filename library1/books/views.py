from django.shortcuts import render, redirect

from books.forms import BookForm

from books.models import Book
from django.template.defaultfilters import title
from django.templatetags.i18n import language

from django.views import View

# Create your views here.

# def home(request):
#     return  render(request,'home.html')

class Home(View):
    def get(self,request):
        return render(request,'home.html')

# def addbooks(request):
#     if request.method=="POST":
#         print(request.POST)
#         print(request.FILES)
#         form_instance=BookForm(request.POST,request.FILES)
#         if form_instance.is_valid():
#             form_instance.save()
#             # data=form_instance.cleaned_data
#             # print(data)
#             # t=data['title']
#             # a=data['author']
#             # p=data['price']
#             # pg=data['pages']
#             # l=data['language']
#             # b=Book.objects.create(title=t,author=a,price=p,pages=pg,language=l)
#             # b.save()
#             # return render(request,'addbooks.html')
#             return redirect('books:viewbooks')


    # if request.method=="GET":
    #     form_instance=BookForm()
    #     context={'form':form_instance}
    #     return render(request,'addbooks.html',context)

class Addbooks(View):
    def post(self,request):
        form_instance=BookForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('books:viewbooks')

    def get(self,request):
        form_instance=BookForm()
        context={'form':form_instance}
        return render(request,'addbooks.html',context)

#
# def viewbooks(request):
#     b=Book.objects.all() #to read all record from table
#     context={'books':b}
#     return render(request,'viewbooks.html',context)

class Viewbooks(View):
    def get(self,request):
        b=Book.objects.all()
        context={'books':b}
        return render(request,'viewbooks.html',context)


# def viewdetails(request,i):
#     if request.method=="GET":
#         b=Book.objects.get(id=i)
#         context={'books':b}
#         return render(request,'viewdetails.html',context)

class Viewdetails(View):
    def get(self,request,i):
        b = Book.objects.get(id=i)
        context = {'books': b}
        return render(request, 'viewdetails.html', context)


# def editbook(request,i):
#     if request.method == "POST":
#         b=Book.objects.get(id=i)
#         form_instance = BookForm(request.POST, request.FILES,instance=b)
#         if form_instance.is_valid():
#             form_instance.save()
#             return redirect('books:viewbooks')
#
#     if request.method=="GET":
#         b=Book.objects.get(id=i)
#         form_instance=BookForm(instance=b)
#         context={'form':form_instance}
#         return render(request,'editbook.html',context)

class Editbook(View):
    def post(self,request,i):
        b = Book.objects.get(id=i)
        form_instance = BookForm(request.POST, request.FILES, instance=b)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('books:viewbooks')
    def get(self,request,i):
        b=Book.objects.get(id=i)
        form_instance=BookForm(instance=b)
        context={'form':form_instance}
        return render(request,'editbook.html',context)



# def deletebook(request,i):
#     b=Book.objects.get(id=i)
#     b.delete()
#     return redirect('books:viewbooks')

class Deletebook(View):
    def get(self,request,i):
        b=Book.objects.get(id=i)
        b.delete()
        return redirect('books:viewbooks')

from django.db.models import Q

class Searchview(View):
    def get(self,request):
        query=request.GET['q']
        # print(query)
        if query:
            # b=Book.objects.filter(Q(author=query)|Q(title=query)|Q(language=query))
            #Q object -- syntax used to add logical or ,not ,and in ORM query
            # field lookup
            b=Book.objects.filter(Q(author__icontains=query)|Q(title__icontains=query)|Q(language__icontains=query))
            context={'book':b}
            return render(request,'search.html',context)
