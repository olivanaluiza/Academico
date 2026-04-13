from django.contrib import admin
from .models import *
from django.contrib import admin

class MatriculaInline(admin.TabularInline):
    model = Matricula
    extra = 1

class FrequenciaInlinePessoa(admin.TabularInline):
    model = Frequencia
    extra = 1

class OcorrenciaInlinePessoa(admin.TabularInline):
    model = Ocorrencia
    extra = 1

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'cidade')
    search_fields = ('nome', 'cpf')
    inlines = [MatriculaInline, FrequenciaInlinePessoa, OcorrenciaInlinePessoa]

admin.site.register(Pessoa, PessoaAdmin)

class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1

class OcupacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    inlines = [PessoaInline]

admin.site.register(Ocupacao, OcupacaoAdmin)

class InstituicaoInlineCidade(admin.TabularInline):
    model = InstituicaoEnsino
    extra = 1

class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'uf')
    inlines = [InstituicaoInlineCidade]

admin.site.register(Cidade, CidadeAdmin)

class CursoInlineInstituicao(admin.TabularInline):
    model = Curso
    extra = 1

class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade')
    inlines = [CursoInlineInstituicao]

admin.site.register(InstituicaoEnsino, InstituicaoAdmin)

class CursoInlineArea(admin.TabularInline):
    model = Curso
    extra = 1

class DisciplinaInlineArea(admin.TabularInline):
    model = Disciplina
    extra = 1

class AreaSaberAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    inlines = [CursoInlineArea, DisciplinaInlineArea]

admin.site.register(AreaSaber, AreaSaberAdmin)

class CursoDisciplinaInline(admin.TabularInline):
    model = CursoDisciplina
    extra = 1

class AvaliacaoInlineCurso(admin.TabularInline):
    model = Avaliacao
    extra = 1

class MatriculaInlineCurso(admin.TabularInline):
    model = Matricula
    extra = 1

class FrequenciaInlineCurso(admin.TabularInline):
    model = Frequencia
    extra = 1

class OcorrenciaInlineCurso(admin.TabularInline):
    model = Ocorrencia
    extra = 1

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'instituicao', 'area_saber')
    inlines = [
        CursoDisciplinaInline,
        AvaliacaoInlineCurso,
        MatriculaInlineCurso,
        FrequenciaInlineCurso,
        OcorrenciaInlineCurso
    ]

admin.site.register(Curso, CursoAdmin)

class AvaliacaoInlineDisciplina(admin.TabularInline):
    model = Avaliacao
    extra = 1

class FrequenciaInlineDisciplina(admin.TabularInline):
    model = Frequencia
    extra = 1

class OcorrenciaInlineDisciplina(admin.TabularInline):
    model = Ocorrencia
    extra = 1

class CursoDisciplinaInlineDisciplina(admin.TabularInline):
    model = CursoDisciplina
    extra = 1

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'area_saber')
    inlines = [
        AvaliacaoInlineDisciplina,
        FrequenciaInlineDisciplina,
        OcorrenciaInlineDisciplina,
        CursoDisciplinaInlineDisciplina
    ]

admin.site.register(Disciplina, DisciplinaAdmin)

class AvaliacaoInlineTipo(admin.TabularInline):
    model = Avaliacao
    extra = 1

class AvaliacaoTipoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    inlines = [AvaliacaoInlineTipo]

admin.site.register(AvaliacaoTipo, AvaliacaoTipoAdmin)

class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'curso', 'instituicao', 'data_inicio')
    search_fields = ('pessoa__nome', 'curso__nome')

admin.site.register(Matricula, MatriculaAdmin)

class FrequenciaAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'curso', 'disciplina', 'numero_faltas')

admin.site.register(Frequencia, FrequenciaAdmin)

class OcorrenciaAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'curso', 'disciplina', 'data')
    search_fields = ('descricao',)

admin.site.register(Ocorrencia, OcorrenciaAdmin)

class MatriculaInlineTurma(admin.TabularInline):
    model = Matricula
    extra = 1

class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    inlines = [MatriculaInlineTurma]

admin.site.register(Turma, TurmaAdmin)

class TurnosAdmin(admin.ModelAdmin):
    list_display = ('nome',)

admin.site.register(Turnos, TurnosAdmin)