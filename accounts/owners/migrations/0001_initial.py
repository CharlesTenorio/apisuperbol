# Generated by Django 3.0.3 on 2021-02-15 15:23

import core.base.fields
import core.base.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=120)),
                ('street_number', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=80)),
                ('state', models.CharField(max_length=2)),
                ('complement', models.CharField(blank=True, max_length=250)),
                ('zip_code', core.base.fields.ZipCodeField(max_length=9, validators=[core.base.validators.validate_zip_code])),
                ('phone_prefix', models.CharField(max_length=2)),
                ('phone_number', models.CharField(max_length=9)),
                ('is_natural', models.CharField(choices=[('CPF', 'Pessoa Física'), ('CNPJ', 'Pessoa Jurídica')], default='CPF', max_length=5, verbose_name='Tipo de pessoa')),
                ('cpf_cnpj', core.base.fields.CnpjField(max_length=18, validators=[core.base.validators.validate_cnpj], verbose_name='Documento')),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Proprietario',
                'verbose_name_plural': 'Proprietários',
            },
        ),
    ]
