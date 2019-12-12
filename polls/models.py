import datetime

from django.db import models
from django.utils import timezone

# Creo el modelo
class Question(models.Model):
    question_text = models.CharField(max_length=200) #campos de caracteres
    pub_date = models.DateTimeField('date published') #var de tiempo y fecha
    #las instancias Field (question_text y pub_date)
    #seran usadas como nombre de columna por la BD
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    #ForeignKey indica a django q cd Choice se relaciona con una Question
    #Charfield, hay que asignarle un max-length se usa en la BD y en la validacion
    #Votes se fijo por defecto el valor 0, puede tener otros argumentos
    def __str__(self):
        return self.choice_text
