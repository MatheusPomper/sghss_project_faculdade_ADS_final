from rest_framework import serializers
from .models import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ["id", "nome", "cpf", "data_nascimento", "telefone", "criado_em"]
        read_only_fields = ["id", "criado_em"]
