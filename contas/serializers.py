from rest_framework import serializers

from contas.models import Conta


class ContaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Conta
        # fields = '__all__'
        fields = [
            'id',
            'url',
            'data_leitura_relogio',
            'numero_leitura',
            'kw',
            'valor',
            'data_pagamento',
            'media_consumo',
        ]
