from django.db import models


class Conta(models.Model):
    class Meta:
        db_table = 'contas'
        verbose_name = 'Conta de Luz'

    data_leitura_relogio = models.DateField()
    numero_leitura = models.PositiveIntegerField()
    kw = models.PositiveIntegerField()
    valor = models.FloatField()
    data_pagamento = models.DateField()
    media_consumo = models.FloatField()
