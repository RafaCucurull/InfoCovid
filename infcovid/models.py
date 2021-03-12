from django.db import models
from users import models as userModels
from django.utils import timezone


class Pregunta(models.Model):
    enunciat = models.CharField(max_length=100)
    resposta = models.CharField(max_length=100)

class Resultat(models.Model):
    resultat = models.CharField(max_length=100)


class Test(models.Model):
    data = models.DateTimeField(default = timezone.now())
    usuari = models.ForeignKey(userModels.CustomUser, on_delete=models.CASCADE)
    resultat = models.ForeignKey(Resultat, on_delete=models.CASCADE)

class PreguntesTest(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)

class RespostaConsulta(models.Model):
    resposta = models.CharField(max_length=100)

class Consulta(models.Model):
    consulta = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    resposta = models.ForeignKey(RespostaConsulta, on_delete=models.CASCADE, null = True)
    usuari = models.ForeignKey(userModels.CustomUser, on_delete=models.CASCADE, null = True)
