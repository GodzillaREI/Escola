from django.contrib import admin
from escola.models import Estudante, Curso

# Configuração do ModelAdmin para o modelo Estudante
class EstudantesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular')
    list_display_links = ('id', 'nome')
    list_per_page = 20
    search_fields = ('nome',)

# Configuração do ModelAdmin para o modelo Curso
class CursosAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'descricao')
    list_display_links = ('id', 'codigo')
    search_fields = ('codigo',)

# Registro dos modelos no admin
admin.site.register(Estudante, EstudantesAdmin)
admin.site.register(Curso, CursosAdmin)
