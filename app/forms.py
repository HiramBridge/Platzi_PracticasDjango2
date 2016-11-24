from django import forms
from django.forms import ModelForm
from models import *

# Creacion de las formas

class EnlaceForm(ModelForm):
	class Meta:
		model = Enlace
		fields = ('titulo', 'enlace', 'categoria','imagen',)