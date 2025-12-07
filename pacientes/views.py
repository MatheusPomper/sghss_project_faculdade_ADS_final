from rest_framework import viewsets, permissions
from .models import Paciente
from .serializers import PacienteSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all().order_by('-criado_em')
    serializer_class = PacienteSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"
