from django.shortcuts import render

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
