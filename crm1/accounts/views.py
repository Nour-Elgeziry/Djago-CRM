# classes that url go to to trigger and render templates
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("Home Page")

def products(request):
    return HttpResponse("Products")

def customer(request):
    return HttpResponse("Customer")
    
    
    
    
    
    