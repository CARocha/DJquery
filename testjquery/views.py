# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from django.utils import simplejson as json
from testjquery.models import Usuario
from testjquery.forms import UsuarioForm

def index(request):
	form = UsuarioForm()
	return render_to_response('index.html',
		                     RequestContext(request, locals()))

def guardar_user(request):
	if request.is_ajax():
		form = UsuarioForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse(json.dumps("exito"),
                							mimetype="application/json")
		else:
			return HttpResponse(json.dumps("errores"),
                							mimetype="application/json")

def buscar_user(request):
	omg = request.GET.get('user', None)
	#print repr(request.GET)
	#print omg
	buscar = Usuario.objects.filter(nombre__icontains=omg).values_list('nombre','apellido','edad')
	
	return HttpResponse(json.dumps(list(buscar)),
		                mimetype="application/json")

def modificar_user(request, id):
	ver = get_object_or_404(Usuario, id=id)
	if request.is_ajax():
		form = UsuarioForm(instance=ver)
		if form.is_valid():
			form.save()
	return HttpResponse(json.dumps("updated"),
                	mimetype="application/json")

def eliminar_user(request, id):
	usuario = Usuario.objects.filter(id=id)
	if request.user.is_authenticated():
		usuario.delete()
	return HttpResponse(json.dumps("deleted"),
		               mimetype="application/json")