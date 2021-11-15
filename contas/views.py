from rest_framework import viewsets

from contas.models import Conta
from contas.serializers import ContaSerializer


class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer
