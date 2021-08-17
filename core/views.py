from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Web Personal</h1><h2>Home</h2>")

def about(request):
    return HttpResponse("<h3> Acerca de</h3>")    

def porfolio (request):
    return HttpResponse("Porfolio")

def contact(request):
    return HttpResponse("Contacto")
