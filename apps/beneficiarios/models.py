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
    # Usa a constante para definir o tamanho máximo do campo nome
    nome = models.CharField(max_length=MAX_LENGTH)
    # Usa o validador para verificar o formato do CPF
    cpf = models.CharField(max_length=11, unique=True, validators=[cpf_validator])
    # Repete os campos e os validadores do endereço na classe Beneficiario
    logradouro = models.CharField(max_length=MAX_LENGTH)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(max_length=MAX_LENGTH, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=8, validators=[cep_validator])
    # Usa o validador para verificar o formato do telefone
    telefone_contato = models.CharField(max_length=15, validators=[telefone_validator])
    prefeitura_associado = models.ForeignKey(Prefeitura, on_delete=models.CASCADE)

    def __str__(self):
        # Cria um método para formatar o endereço na classe Beneficiario
        # Usa uma lista para armazenar as partes do endereço
        endereco = []
        # Adiciona o logradouro e o número
        endereco.append(f"{self.logradouro}, {self.numero}")
        # Se houver complemento, adiciona também
        if self.complemento:
            endereco.append(self.complemento)
        # Adiciona o bairro, a cidade, o estado e o cep
        endereco.append(self.bairro)
        endereco.append(f"{self.cidade} - {self.estado}")
        endereco.append(self.cep)
        # Retorna o endereço separado por vírgulas
        endereco = ", ".join(endereco)
        # Retorna o nome e o endereço do beneficiário
        return f"{self.nome} - {endereco}"
