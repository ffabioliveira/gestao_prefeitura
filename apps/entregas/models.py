from django.db import models
from apps.beneficiarios.models import Beneficiario
from apps.pipeiros.models import Pipeiro
from django.utils.translation import gettext_lazy as _

# Define uma classe para o status da entrega, usando o Django Enum
class StatusEntrega(models.TextChoices):
    PENDENTE = 'P', _('Pendente')
    CONCLUIDA = 'C', _('Concluída')
    EM_ANDAMENTO = 'E', _('Em andamento')
    CANCELADA = 'X', _('Cancelada')

class EntregaAgua(models.Model):
    beneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)
    pipeiro_responsavel = models.ForeignKey(Pipeiro, on_delete=models.CASCADE)
    data_hora_agendamento = models.DateTimeField()
    # Usa o Django Enum para definir o campo status_entrega
    status_entrega = models.CharField(
        max_length=1,
        choices=StatusEntrega.choices,
        default=StatusEntrega.PENDENTE,
    )
    quantidade_agua_entregue_litros = models.PositiveIntegerField(null=True, blank=True)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"Entrega para {self.beneficiario} agendada em {self.data_hora_agendamento}"
