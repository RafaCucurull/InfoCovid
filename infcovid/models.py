from django.db import models
from users import models as userModels
from django.utils import timezone


class Pregunta(models.Model):
    enunciat = models.CharField(max_length=100)
    RESPOSTA_CHOICES = (
        ('YES', 'Sí'),
        ('NO', 'No'),
    )
    resposta = models.CharField(max_length=9,
                                choices=RESPOSTA_CHOICES,
                                default='YES')


class Resultat(models.Model):
    resultat = models.CharField(max_length=100)


class Test(models.Model):
    Pregunta = models.ManyToManyField(Pregunta)
    data = models.DateTimeField(default=timezone.now())
    usuari = models.ForeignKey(userModels.CustomUser, on_delete=models.CASCADE)
    resultat = models.ForeignKey(Resultat, on_delete=models.CASCADE)


class RespostaConsulta(models.Model):
    resposta = models.CharField(max_length=100)


class Consulta(models.Model):
    consulta = models.CharField(max_length=100)
    CATEGORIA_CHOICES = (
        ('I', 'Informació'),
        ('RE', 'Restriccions'),
        ('MS', 'Mascaretes'),
        ('SI', 'Símptomes'),
    )
    categoria = models.CharField(max_length=9,
                                 choices=CATEGORIA_CHOICES,
                                 default='I')
    resposta = models.ForeignKey(RespostaConsulta, on_delete=models.CASCADE, null=True)
    usuari = models.ForeignKey(userModels.CustomUser, on_delete=models.CASCADE, null=True)
