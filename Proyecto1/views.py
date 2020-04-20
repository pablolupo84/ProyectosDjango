from django.http import HttpResponse
import datetime

def saludo(request): #Primera Vista
	documento="""<html>
	<body>
	<h1>
	Hola Alumnos esta es nuestra primera pagina con Django
	</h1>
	</body>
	</html>"""
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