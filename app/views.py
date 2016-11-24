from django.shortcuts import render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
from models import *
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from forms import *		
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView

from django.views.decorators.cache import cache_page

#Forma adaptable a una solicitud
@login_required
def add(request):
	categorias = Categoria.objects.all()
	if request.method == "POST":
		form = EnlaceForm(request.POST, request.FILES)

		if form.is_valid():
			enlace = form.save(commit = False)
			enlace.usuario = request.user
			form.save()
			return HttpResponseRedirect("/")

	else:
		form = EnlaceForm()

		template = "form.html"
		return render(request,template,locals())


#@cache_page(6000)
def home(request):
	categorias = Categoria.objects.all()
	enlaces = Enlace.objects.order_by("-votos").all()
	template = "index.html"
	return render(request,template,locals())

#botonera de votaciones	

@login_required
def minus(request, id_enlace):
	enlace = Enlace.objects.get(pk = id_enlace)
	enlace.votos = enlace.votos - 1
	enlace.save()
	return HttpResponseRedirect("/")
	
@login_required
def plus(request, id_enlace):
	enlace = Enlace.objects.get(pk = id_enlace)
	enlace.votos = enlace.votos + 1
	enlace.save()
	return HttpResponseRedirect("/")

#cambiar categorias y filtrar texts por categorias	

def categoria(request, id_categoria):
	categorias = Categoria.objects.all()
	cat = get_object_or_404(Categoria, pk = id_categoria)
	enlaces = Enlace.objects.filter(categoria = cat)
	template = "index.html"
	return render(request,template, locals())	

#primera implementacion en views	


def hora_actual(request):
	now = datetime.now()
	return render_to_response('hora.html', {'hora':now})


class EnlaceListView(ListView):
	model = Enlace
	context_object_name = 'enlaces'
	def get_template_names(self):
		return 'index.html'	

class EnlaceDetailView(DetailView):
	model = Enlace
	def get_template_names(self):
		return 'index.html'		

from serializers import EnlaceSerializer, UserSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User

class EnlaceViewSet(viewsets.ModelViewSet):
	queryset = Enlace.objects.all()
	serializer_class = EnlaceSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer	

