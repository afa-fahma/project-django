from django.shortcuts import render ,redirect
from .models import book
from .forms import BookForm,userRegistrationform

# Create your views here.
# from django.http import HttpResponse
# def home(request):
#     return HttpResponse("Helloworld")
# def about(request):
#     return HttpResponse("this is the about section")

def home(request):
    data=['python','django','flutter','react']
    return render (request,'home.html',{'a':data})
def about(request):
    datas={
        "name":'afa fahma',
        "age" :20,
        "place":'kalikavu'

    }

    return render(request,'about.html',datas)
def contact(request):
    return render(request,'contact.html')
def ViewBook(request):
    a=book.objects.all()
    return render(request,'ViewBook.html',{"ab":a})
    
def addbook(request):
    a=BookForm(request.POST or None)
    if a.is_valid():
        a.save()
        return redirect('ViewBook')
    return render(request,'addbook.html',{"abc":a})
def update_book(request,id):
    a=book.objects.get(id=id)
    b=BookForm(request.POST or None,instance=a)
    if b.is_valid():
        b.save()
        return redirect(ViewBook)
    return render(request,'updatebook.html',{"ab":b})
def delete_book(request,id):
    a=book.objects.get(id=id)
    if request.method=='POST':
        a.delete()
        return redirect(ViewBook)
    return render (request,'deletebook.html',{"abc":a})
def register(request):
    form=userRegistrationform(request.POST or None)
    if request.method=='POST' and form.is_valid():
        form.save()
        return redirect('ViewBook')
    return render (request,'register.html',{"form":form})
