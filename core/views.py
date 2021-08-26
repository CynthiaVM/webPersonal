from django.shortcuts import render, HttpResponse

html_base = """
    <h1>Mi Web Personal</h1>
    <ul>
        <li><a href="/">Portada</a></li>
        <li><a href="/about/">Acerca de</a></li>
        <li><a href="/contact/">Contacto</a></li>
    </ul>
"""

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def portfolio(request):
    return render(request, "core/portfolio.html")

def contact(request):
    return render(request, "core/contact.html") 



#html_base= ""

#def home(request):
    #return HttpResponse("<h1>Home</h1>")
#def about(request):
    #return HttpResponse("<h1> Acerca de</h1>")    

#def porfolio (request):
    #return HttpResponse("Porfolio")

#def contact(request):
    #return HttpResponse("Contacto")
