from rest_framework import serializers
from .models import Consulta
from pacientes.models import Paciente

class ConsultaSerializer(serializers.ModelSerializer):
    paciente = serializers.PrimaryKeyRelatedField(queryset=Paciente.objects.all())

    class Meta:
        model = Consulta
        fields = ["id", "paciente", "usuario", "data_consulta", "horario", "observacoes", "criado_em", "cancelado", "motivo_cancelamento"]
        read_only_fields = ["id", "usuario", "criado_em", "cancelado", "motivo_cancelamento"]

    def create(self, validated_data):
        request = self.context.get("request")
        if request and request.user and request.user.is_authenticated:
            validated_data["usuario"] = request.user
        return super().create(validated_data)
