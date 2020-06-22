from django.shortcuts import render
from .models import contactdata

# Create your views here.


def index(request):
    return render(request,'index.html')

def gallery(request):
    return render(request,'gallery.html')

def blog(request):
    return render(request,'blog.html')
def services(request):
    return render(request,'services.html')
def contact(request):
    return render(request,'contact.html')

def aboutus(request):
    return render(request,'aboutus.html')

def contactsubmit(request):
    name=request.POST['name']
    email = request.POST['email']
    msg= request.POST['msg']

    ref=contactdata(name=name,emailid=email,msg=msg)
    ref.save()
    return render(request,'contact.html')