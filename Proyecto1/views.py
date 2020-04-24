from django.http import HttpResponse
import datetime
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):
	"""docstring for Persona"""
	def __init__(self, nombre,apellido):
		self.nombre=nombre
		self.apellido=apellido
		

def saludo(request):

	# C:/ProyectosDjango/Proyecto1/Proyecto1/plantillas/plantilla_1.html
	#nombre="Juan"
	#apellido="Perez"

	temasDelCurso=["Formularios","Plantillas","Vistas","Despliegue App"]
	p1=Persona("Profe Pablo","Lupo")
	hora_actual=datetime.datetime.now()

	# doc_externo=open("C:/ProyectosDjango/Proyecto1/Proyecto1/plantillas/plantilla_1.html")
	# plt=Template(doc_externo.read())
	# doc_externo.close()
	
	# doc_externo=get_template('plantilla_1.html')
	# ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":hora_actual,"temas":temasDelCurso})

	# documento=plt.render(ctx)
	# documento=doc_externo.render({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":hora_actual,"temas":temasDelCurso})
	return render(request,'plantilla_1.html',{"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":hora_actual,"temas":temasDelCurso})

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

def cursoC(request):
	fecha_actual=datetime.datetime.now()

	return render(request,"cursoC.html",{"damefecha":fecha_actual})

def cursoPython(request):
	fecha_actual=datetime.datetime.now()

	return render(request,"cursoPython.html",{"damefecha":fecha_actual})
