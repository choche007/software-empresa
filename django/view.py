from django.http import HttpResponse
import datetime

def hola(request):
    return HttpResponse("Hola amiguillos esto es perfectijillo ")

def malditoflanders(request):

    pagina="""
    <html>
    <body>
        <h1> Saludirijillos ALUMNILLOS!!!!
        </h1>
    </body>
    </html>
    """
    return HttpResponse(pagina)

def calculo_edad(request ,edad, agno):
    
    #edad_actual=41
    periodo=agno-2022
    edad_fut=edad+periodo
    documento="<html><body><h2> en el año %s tendras %s años </h2></body></html>"%(agno,edad_fut)

    return HttpResponse(documento)
	
	