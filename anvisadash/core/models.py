from django.db import models
from django.contrib.auth.models import User

class Processo(models.Model):
    medicamento = models.CharField(
        "Medicamento",
        max_length=100,
        default="",
        blank=False,
        help_text="Ex.: Tylenol"
    )
    codigo_processo = models.CharField(
        "Codigo do Processo",
        max_length=100,
        default="",
        blank=False,
        help_text="Ex.: 250000112969983"
    )

class Peticionamento(models.Model):
    processo = models.OneToOneField(Processo, on_delete=models.CASCADE)
    expediente = models.CharField(
        "Expediente (Dt. Expediente)",
        max_length=100,
        default="",
        blank=False,
        help_text="Ex.: 0530391/19-5 (14/06/2019)"
    )
    n_protocolo = models.CharField(
        "Numero do Protocolo",
        max_length=100,
        default="",
        blank=False,
        help_text="Ex.: 25352.408326/2019-31"
    )
    assunto = models.CharField(
        "Assunto",
        max_length=400,
        default="",
        blank=False,
        help_text="Ex.: 10708 - RPF/Sumário - Renovação de Registro - Medicamento Novo"
    )
    encontrase = models.CharField(
        "Encontra-se",
        max_length=300,
        default="",
        blank=False,
        help_text="Ex.: GEAAR - GERÊNCIA DE ANÁLISE E AVALIAÇÃO DE RISCO"
    )
    data_encontrase =models.CharField(
        "Encontra-se desde:",
        max_length=100,
        default="",
        blank=False,
        help_text="Ex.: 14/06/2019"
    )
    situacao = models.CharField(
        "Situação",
        max_length=1000,
        default="",
        blank=False,
        help_text="Ex.: Distribuído para a área responsável"
    )
    publicacao = models.CharField(
        "Medicamento",
        max_length=100,
        default="",
        blank=False,
        help_text="Ex.: Não Publicado ou 1.513 - 14/06/2018"
    )

class Tarefas(models.Model):
    responsavel = models.OneToOneField(User, on_delete=models.CASCADE)
    texto_tarefa = models.CharField(
        "Titulo da Tarefa",
        max_length=100,
        default="",
        blank=False,
        help_text="Ex.: ACME Inc"
    )
    texto_tarefa = models.CharField(
        "Descricao da Tarefa",
        max_length=100,
        default="",
        blank=False,
        help_text="Ex.: ACME Inc"
    )


# Criar triggers de Tarefas
# Criar triggers de Peticionamento
