from rest_framework import serializers
from estoque.models import EstoqueInterno

class EstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstoqueInterno
        fields = ['id', 'nome', 'valor']
