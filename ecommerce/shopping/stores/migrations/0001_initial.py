# Generated by Django 3.0.3 on 2021-02-15 15:23

import core.base.fields
import core.base.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('owners', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=250, verbose_name='Razão social')),
                ('fantasy_name', models.CharField(blank=True, max_length=250, null=True, verbose_name='Nome Fantasia')),
                ('cpf_cnpj', core.base.fields.CpfCnpjField(max_length=18, validators=[core.base.validators.validate_cpf_cnpj], verbose_name='Documento')),
                ('type', models.SmallIntegerField(choices=[(0, 'Informal'), (1, 'MEI'), (2, 'Individual'), (3, 'Eireli'), (4, 'LTDA')], default=2, verbose_name='TIpo de empresa')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owners.Owner', verbose_name='Proprietário')),
            ],
        ),
    ]
