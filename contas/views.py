from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination

from contas.models import Conta
from contas.serializers import ContaSerializer
from django.db.models import Min, Max


class ContaPagination(PageNumberPagination):
    page_size = 12

    def get_paginated_response(self, data):
        return Response({
            'num_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'count': self.page.paginator.count,
            'results': data
        })


class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer
    pagination_class = ContaPagination


@api_view(http_method_names=['GET'])
def min_max_valor(request):
    min_max_valor = Conta.objects.aggregate(
        min_valor=Min('valor'), max_valor=Max('valor'))

    return Response({
        'minValor': min_max_valor['min_valor'],
        'maxValor': min_max_valor['max_valor']
    })
