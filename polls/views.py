from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import Question
#creo la primera vista

def index(request): #muestra ultimas preguntas
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

    #return HttpResponse("Hola Mundo. Estás en el índice de encuestas.")

#agrego vistas de preguntas
def detail(request, question_id):  #txt de preg sin resul y con form para vot
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id): #muestra res de 1 preg partic
    response = "Estás viendo los resultados de la pregunta %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):  #gestiona la votacion en una pag espcif
    return HttpResponse("Estás votando una pregunta %s." % question_id)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
