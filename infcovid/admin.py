from django.contrib import admin
from .models import Pregunta, Test, RespostaConsulta, Consulta


class PreguntaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Pregunta, PreguntaAdmin)


class TestAdmin(admin.ModelAdmin):
    pass


admin.site.register(Test, TestAdmin)


class RespostaConsultaAdmin(admin.ModelAdmin):
    pass


admin.site.register(RespostaConsulta, RespostaConsultaAdmin)


class ConsultaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Consulta, ConsultaAdmin)
