from django.http import HttpResponse
import datetime
from django.template import Template, Context

def bienvenido1(request):
    return HttpResponse("Bienvenido a la comision django de Mario")

def bienvenido2(request, nombre):
    respuesta = f"Bienvenido {nombre} a la comision 50500"
    return HttpResponse(respuesta)

def bienvenido3(request):

   hoy = datetime.datetime.now()   

   respuesta = f"""

      <html>

      <h1>Bienvenidos al curso de Django</h1>

      <h2>Esta es la comisión 50200</h2>

      <h3>Hoy es {hoy}</h3>

      <html>"""

   return HttpResponse(respuesta)

def calcularbruto(request, neto):
    neto=int(neto)
    respuesta = f"<html><h1>El bruto de la factura es {neto*1.21} </h1></html>"
    return HttpResponse(respuesta)

def bienvenido_template(request):
    miHtml = open("C:/Coder/Clase_17/proyecto1/proyecto1/plantillas/bienvenido.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    respuesta = plantilla.render(miContexto)
    return HttpResponse(respuesta)