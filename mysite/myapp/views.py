from django.http import HttpResponse                   
from django.shortcuts import render   


def index(request):
    return render(request, 'myapp/peticion.html', {})

def documentacion(request):
    return render(request, 'myapp/documentacion.html', {})

# def documentacion(request):
#     pdf = render.pdf("myapp/documentacion.html")
#     return HttpResponse(request, pdf,content_type = "application/pdf")

def estudiante(request):
    return render(request, 'myapp/estudiante.html', {})