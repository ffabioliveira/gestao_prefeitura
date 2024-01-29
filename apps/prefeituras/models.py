from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# Define uma constante para o tamanho máximo dos campos de texto
MAX_LENGTH = 100

# Define um validador para o formato do telefone
telefone_validator = RegexValidator(
    regex=r"^\(\d{2}\) \d{4,5}-\d{4}$",
    message="O telefone deve estar no formato (XX) XXXX-XXXX ou (XX) XXXXX-XXXX"
)

class Prefeitura(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    # Usa a constante para definir o tamanho máximo dos campos
    prefeitura = models.CharField(max_length=MAX_LENGTH)
    responsavel = models.CharField(max_length=MAX_LENGTH)
    # Usa o validador para verificar o formato do telefone
    telefone_responsavel = models.CharField(max_length=15, validators=[telefone_validator])

    # Define os campos do endereço seguindo o padrão dos correios
    logradouro = models.CharField(max_length=MAX_LENGTH)
    numero = models.PositiveIntegerField()
    complemento = models.CharField(max_length=MAX_LENGTH, blank=True)
    bairro = models.CharField(max_length=MAX_LENGTH)
    cidade = models.CharField(max_length=MAX_LENGTH)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)

    def __str__(self):
        return self.prefeitura

    # Define um método para formatar o endereço completo
    def get_endereco(self):
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
        return ", ".join(endereco)
