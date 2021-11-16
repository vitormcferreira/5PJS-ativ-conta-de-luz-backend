from rest_framework import viewsets
from rest_framework.response import Response

from contas.models import Conta
from contas.serializers import ContaSerializer
from django.db.models import Min, Max


class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer

    def list(self, request, *args, **kwargs):
        contas = self.get_queryset()
        contas_ser = self.get_serializer(contas, many=True)

        min_max_valor = self.queryset.aggregate(
            min_valor=Min('valor'), max_valor=Max('valor'))

        return Response({
            'contas': contas_ser.data,
            'minMaxValor': {
                'minValor': min_max_valor['min_valor'],
                'maxValor': min_max_valor['max_valor']
            },
        })
