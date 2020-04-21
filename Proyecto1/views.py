from django.http import HttpResponse
import datetime
from django.template import Template,Context

class Persona(object):
	"""docstring for Persona"""
	def __init__(self, nombre,apellido):
		self.nombre=nombre
		self.apellido=apellido
		

def saludo(request):

	# C:/ProyectosDjango/Proyecto1/Proyecto1/plantillas/plantilla_1.html
	#nombre="Juan"
	#apellido="Perez"
	p1=Persona("Profe Pablo","Lupo")
	hora_actual=datetime.datetime.now()

	doc_externo=open("C:/ProyectosDjango/Proyecto1/Proyecto1/plantillas/plantilla_1.html")

	plt=Template(doc_externo.read())
	doc_externo.close()
	
	ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":hora_actual})

	documento=plt.render(ctx)
	return HttpResponse(documento)

def despedida(request): #Primera Vista
	return HttpResponse("Hasta luego Alumnos de Django")

def damefecha(request):
	fecha_actual=datetime.datetime.now()

	documento="""<html>
	<body>
	<h2>
	Fecha y Hora Actuales: {}
	</h2>
	</body>
	</html>""".format(fecha_actual)

	return HttpResponse(documento)

def calculaedad(request,edad,agno):
	# edadActual=18
	periodo=agno-2019
	edadFutura=edad+periodo
	documento="<html><body><h2> En el año {} tendras: {} años</h2></body></html>".format(agno,edadFutura)
	return HttpResponse(documento)	