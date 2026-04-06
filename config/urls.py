from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('pessoa/', PessoaView.as_view(), name='pessoa'),
    path('ocupacao/', OcupacaoView.as_view(), name='ocupacao'),
    path('instituicao-ensino/', InstituicaoEnsinoView.as_view(), name='instituicao_ensino'),
    path('area-saber/', AreaSaberView.as_view(), name='area_saber'),
    path('curso/', CursoView.as_view(), name='curso'),
    path('turma/', TurmaView.as_view(), name='turma'),
    path('disciplina/', DisciplinaView.as_view(), name='disciplina'),
    path('matricula/', MatriculaView.as_view(), name='matricula'),
    path('avaliacao/', AvaliacaoView.as_view(), name='avaliacao'),
    path('frequencia/', FrequenciaView.as_view(), name='frequencia'),
    path('turnos/', TurnosView.as_view(), name='turnos'),
    path('cidade/', CidadeView.as_view(), name='cidade'),
    path('ocorrencia/', OcorrenciaView.as_view(), name='ocorrencia'),
    path('curso-disciplina/', CursoDisciplinaView.as_view(), name='curso_disciplina'),
    path('avaliacao-tipo/', AvaliacaoTipoView.as_view(), name='avaliacao_tipo'),
]
