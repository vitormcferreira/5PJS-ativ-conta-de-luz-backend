from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from contas.models import Conta
from contas.serializers import ContaSerializer
from django.db.models import Min, Max


class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer


@api_view(http_method_names=['GET'])
def min_max_valor(request):
    min_max_valor = Conta.objects.aggregate(
        min_valor=Min('valor'), max_valor=Max('valor'))

    return Response({
        'minValor': min_max_valor['min_valor'],
        'maxValor': min_max_valor['max_valor']
    })
