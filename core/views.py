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
    return HttpResponse(html_base + """
        <h2>Bienvenidos</h2>
        <p>Esto es la portada.</p>
    """)

def about(request):
    return HttpResponse(html_base + """
        <h2>Acerca de</h2>
        <p>Mi nombre es Cynthia y estoy probando Django!</p>
    """)

def contact(request):
    return HttpResponse(html_base + """
        <h2>Contacto</h2>
        <p>Aquí os dejo mi email y mis redes sociales:</p>
        <ul>
            <li><a href="mailto:cynthiamouzo@hotmail.com">Email</a></li>
            <li><a href="https://github.com/CynthiaVM">Github</a></li>
            <li><a href="https://youtube.com">Youtube</a></li>
        </ul>
    """)
#html_base= ""

#def home(request):
    #return HttpResponse("<h1>Home</h1>")
#def about(request):
    #return HttpResponse("<h1> Acerca de</h1>")    

#def porfolio (request):
    #return HttpResponse("Porfolio")

#def contact(request):
    #return HttpResponse("Contacto")
