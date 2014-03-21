from django.test import TestCase
from genre.models import *
import pdb

# Create your tests here.
class GenreTestCase(TestCase):
	def setUp(self):
		subgenre = Genre.objects.create(name='test', description='testcase')
		Genre.objects.create(name='topgenre', description='topgenre', subgenres=[subgenre,])

	def test_subgenre_created(self):
		"""Test if subgenre was succesfull created and added to topgenre"""
		subgenre = Genre.objects.get(name='test')
		topgenre = Genre.objects.get(name='topgenre')

		self.assertIn(subgenre, topgenre.subgenre)