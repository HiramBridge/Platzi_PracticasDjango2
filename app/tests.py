from django.test import TestCase
from models import Categoria, Enlace
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class SimpleTest(TestCase):

	def setUp(self):
		self.categoria = Categoria.objects.create(titulo='Categoria de prueba')
		self.usuario = User.objects.create_user(username='julian', password='barbas')

	def test_es_popular(self):

		
		enlace = Enlace.objects.create(titulo='Prueba', enlace='http://facebook.com', votos=0, categoria=self.categoria, usuario=self.usuario)

		self.assertEqual(enlace.votos, 0)

	def test_views(self):
		res = self.client.get(reverse('home'))
		self.assertEqual(res.status_code, 200)

		self.assertTrue(self.client.login(username='julian', password='barbas'))

		res = self.client.get(reverse('add'))
		self.assertEqual(res.status_code, 200)	