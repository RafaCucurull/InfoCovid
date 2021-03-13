from django.contrib import admin
from .models import Pregunta, Resultat, Test, PreguntaTest, RespostaConsulta, Consulta


class PreguntaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Pregunta, PreguntaAdmin)


class ResultatAdmin(admin.ModelAdmin):
    pass


admin.site.register(Resultat, ResultatAdmin)


class TestAdmin(admin.ModelAdmin):
    pass


admin.site.register(Test, TestAdmin)


class PreguntaTestAdmin(admin.ModelAdmin):
    pass


admin.site.register(PreguntaTest, PreguntaTestAdmin)


class RespostaConsultaAdmin(admin.ModelAdmin):
    pass


admin.site.register(RespostaConsulta, RespostaConsultaAdmin)


class ConsultaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Consulta, ConsultaAdmin)
