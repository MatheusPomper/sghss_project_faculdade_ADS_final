from django.db import models
from django.conf import settings
from pacientes.models import Paciente

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="consultas")
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="consultas")
    data_consulta = models.DateField()
    horario = models.TimeField()
    observacoes = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    cancelado = models.BooleanField(default=False)
    motivo_cancelamento = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["-data_consulta", "-horario"]

    def __str__(self):
        return f"Consulta {self.paciente.nome} em {self.data_consulta} {self.horario}"
