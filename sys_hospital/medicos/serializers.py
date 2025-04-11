from rest_framework import serializers
from .models import Medicos
from enderecos.serializers import EnderecoSerializer
from especializacoes.serializers import EspecializacoesSerializer

class MedicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicos
        fields = '__all__'

