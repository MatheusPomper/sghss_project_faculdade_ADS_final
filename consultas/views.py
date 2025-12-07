from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Consulta
from .serializers import ConsultaSerializer

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=["post"])
    def cancelar(self, request, pk=None):
        consulta = self.get_object()
        if consulta.cancelado:
            return Response({"detail":"Consulta já cancelada."}, status=status.HTTP_400_BAD_REQUEST)
        motivo = request.data.get("motivo", "")
        consulta.cancelado = True
        consulta.motivo_cancelamento = motivo
        consulta.save()
        return Response({"detail":"Consulta cancelada com sucesso."})
