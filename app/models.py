from django.db import models

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

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da ocupação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"

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
