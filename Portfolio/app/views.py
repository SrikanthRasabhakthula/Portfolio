from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def projects(request):
    return render(request,"projects.html")

def certificates(request):
    return render(request,"certificate.html")

def contact(request):
    return render(request,"contact.html")