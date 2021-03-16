from rest_framework import viewsets
from estoque.models import EstoqueInterno
from estoque.serializer import EstoqueSerializer

class EstoqueViewSet(viewsets.ModelViewSet):
    queryset = EstoqueInterno.objects.all()
    serializer_class = EstoqueSerializer

