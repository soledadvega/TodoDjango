from django.shortcuts import render
from django.http import HttpResponse
#creo la primera vista

def index(request):
    return HttpResponse("Hola Mundo. Estás en el índice de encuestas.")
