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

# Define um validador para o formato do CEP
cep_validator = RegexValidator(
    regex=r"^\d{8}$",
    message="O CEP deve ter 8 dígitos numéricos"
)

# Define um validador para o formato do telefone
telefone_validator = RegexValidator(
    regex=r"^\(\d{2}\) \d{4,5}-\d{4}$",
    message="O telefone deve estar no formato (XX) XXXX-XXXX ou (XX) XXXXX-XXXX"
)

class Beneficiario(models.Model):
    nome = models.CharField(max_length=MAX_LENGTH)
    cpf = models.CharField(max_length=11, unique=True, validators=[cpf_validator])
    logradouro = models.CharField(max_length=MAX_LENGTH)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(max_length=MAX_LENGTH, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=8, validators=[cep_validator])
    telefone_contato = models.CharField(max_length=15, validators=[telefone_validator])
    prefeitura_associado = models.ForeignKey(Prefeitura, on_delete=models.CASCADE)

    def __str__(self):
        endereco = []
        endereco.append(f"{self.logradouro}, {self.numero}")
        if self.complemento:
            endereco.append(self.complemento)
        endereco.append(self.bairro)
        endereco.append(f"{self.cidade} - {self.estado}")
        endereco.append(self.cep)
        endereco = ", ".join(endereco)
        return f"{self.nome} - {endereco}"