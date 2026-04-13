from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    uf = models.CharField(max_length=2, verbose_name="UF")

    def __str__(self):
        return f"{self.nome} - {self.uf}"

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da ocupação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    pai = models.CharField(max_length=100, verbose_name="Nome do pai", blank=True, null=True)
    mae = models.CharField(max_length=100, verbose_name="Nome da mãe", blank=True, null=True)
    cpf = models.CharField(max_length=14, verbose_name="CPF", unique=True)
    data_nasc = models.DateField(verbose_name="Data de nascimento")
    email = models.EmailField(verbose_name="Email")

    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.SET_NULL, null=True, verbose_name="Ocupação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome da instituição")
    site = models.URLField(verbose_name="Site", blank=True, null=True)
    telefone = models.CharField(max_length=20, verbose_name="Telefone")

    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Instituição de Ensino"
        verbose_name_plural = "Instituições de Ensino"

class AreaSaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Área do Saber"
        verbose_name_plural = "Áreas do Saber"

class Curso(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome")
    carga_horaria_total = models.IntegerField(verbose_name="Carga horária total")
    duracao_meses = models.IntegerField(verbose_name="Duração (meses)")

    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Área do Saber")
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Instituição de Ensino")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

class AvaliacaoTipo(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tipo de Avaliação"
        verbose_name_plural = "Tipos de Avaliação"

class Disciplina(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome")

    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Área do Saber")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"

class Avaliacao(models.Model):
    descricao = models.CharField(max_length=200, verbose_name="Descrição")

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    avaliacao_tipo = models.ForeignKey(AvaliacaoTipo, on_delete=models.CASCADE, verbose_name="Tipo de Avaliação")

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"

class Turma(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"

class Matricula(models.Model):
    data_inicio = models.DateField(verbose_name="Data de início")
    data_previsao_termino = models.DateField(verbose_name="Data prevista de término")

    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Instituição de Ensino")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.pessoa} - {self.curso}"

    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"

class Frequencia(models.Model):
    numero_faltas = models.IntegerField(verbose_name="Número de faltas")

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")

    def __str__(self):
        return f"{self.pessoa} - {self.disciplina}"

    class Meta:
        verbose_name = "Frequência"
        verbose_name_plural = "Frequências"

class Turnos(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"

class Ocorrencia(models.Model):
    descricao = models.TextField(verbose_name="Descrição")
    data = models.DateField(verbose_name="Data")

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")

    def __str__(self):
        return f"{self.pessoa} - {self.descricao[:50]}"

    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"

class CursoDisciplina(models.Model):
    carga_horaria = models.IntegerField(verbose_name="Carga horária")
    periodo = models.CharField(max_length=50, verbose_name="Período")  # Agora é CharField

    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")

    def __str__(self):
        return f"{self.curso} - {self.disciplina} ({self.periodo})"

    class Meta:
        verbose_name = "Curso Disciplina"
        verbose_name_plural = "Curso Disciplinas"

