from django.db import models
from apps.prefeituras.models import Prefeitura
from django.core.validators import RegexValidator

# Define uma constante para o tamanho máximo dos campos de texto
MAX_LENGTH = 255

# Define um validador para o formato do CPF
cpf_validator = RegexValidator(
    regex=r"^\d{11}$",
    message="O CPF deve ter 11 dígitos numéricos"
)

# Define um validador para o formato da CNH
cnh_validator = RegexValidator(
    regex=r"^\d{11}$",
    message="A CNH deve ter 11 dígitos numéricos"
)

# Define um validador para o formato do telefone
telefone_validator = RegexValidator(
    regex=r"^\(\d{2}\) \d{4,5}-\d{4}$",
    message="O telefone deve estar no formato (XX) XXXX-XXXX ou (XX) XXXXX-XXXX"
)

# Define um validador para o formato da placa do carro
placa_validator = RegexValidator(
    regex=r"^[A-Z]{3}\d{4}$",
    message="A placa do carro deve estar no formato AAA9999"
)

class Pipeiro(models.Model):
    # Usa a constante para definir o tamanho máximo dos campos
    nome = models.CharField(max_length=MAX_LENGTH)
    # Usa os validadores para verificar o formato dos campos
    cpf = models.CharField(max_length=11, unique=True, validators=[cpf_validator])
    cnh = models.CharField(max_length=11, unique=True, validators=[cnh_validator])
    telefone_contato = models.CharField(max_length=15, validators=[telefone_validator])
    capacidade_pipa_litros = models.PositiveIntegerField()
    placa_carro_pipa = models.CharField(max_length=7, validators=[placa_validator])
    fonte_agua = models.CharField(max_length=MAX_LENGTH)
    prefeitura_associado = models.ForeignKey(Prefeitura, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
