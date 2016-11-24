from django.shortcuts import redirect
from random import choice



paises= ['Venezuela', 'Colombia']

def de_donde_vengo(request):
	return choice(paises)

class PaisMiddleware():
	def process_request(self, request):
		pais = de_donde_vengo(request)
		if pais == 'Mexico':
			return redirect('http://facebook.com')	