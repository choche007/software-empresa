from django.http import HttpResponse
from django.shortcuts import render
class libro(object):
    def __init__(self, titulo,autor):
        self.nombre=titulo
        self.autor=autor
def novedades(request):
    return render (request,"plantilla1.html")

def titulos(request):
    return render (request,"plantilla2.html")

def promociones(request):
    return render (request,"plantilla3.html")

	
	