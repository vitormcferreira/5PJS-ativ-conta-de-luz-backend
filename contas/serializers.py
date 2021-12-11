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
    data_leitura_relogio = serializers.DateField(
        input_formats=['%d/%m/%Y'])
    kw = serializers.FloatField(min_value=0)
    valor = serializers.FloatField(min_value=0)
    data_pagamento = serializers.DateField(
        input_formats=['%d/%m/%Y'])
    media_consumo = serializers.FloatField(min_value=0)
