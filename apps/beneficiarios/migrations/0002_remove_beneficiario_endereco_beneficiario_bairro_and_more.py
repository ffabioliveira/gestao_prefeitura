# Generated by Django 5.0.1 on 2024-01-26 22:36

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beneficiario',
            name='endereco',
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='bairro',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='cep',
            field=models.CharField(default=django.utils.timezone.now, max_length=8, validators=[django.core.validators.RegexValidator(message='O CEP deve ter 8 dígitos numéricos', regex='^\\d{8}$')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='cidade',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='complemento',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='estado',
            field=models.CharField(default=django.utils.timezone.now, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='logradouro',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='numero',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Endereco',
        ),
    ]
