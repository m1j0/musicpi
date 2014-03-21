from django.shortcuts import render
from genre.models import Genre
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django import http

# Create your views here.


class ListGenre(ListView):
    model = Genre
    template_name = 'ListGenre.html'


class CreateGenre(CreateView):
    model = Genre
    template_name = 'CreateGenre.html'

    # def post(self, request):
        # import pdb
        # pdb.set_trace()
        # return super(CreateGenre, self).post(request)
