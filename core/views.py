from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Pelu!")

def porfolio (request):
    return HttpResponse("Porfolio")

def contact(request):
    return HttpResponse("Contacto")
