from rest_framework import viewsets, mixins
from estoque.models import EstoqueInterno
from estoque.serializer import EstoqueSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated




class EstoqueViewSet(viewsets.ModelViewSet):
    queryset = EstoqueInterno.objects.all()
    serializer_class = EstoqueSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]




