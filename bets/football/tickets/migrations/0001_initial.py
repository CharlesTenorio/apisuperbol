# Generated by Django 3.0.3 on 2021-04-21 19:58

import core.base.fields
import core.base.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('odds', '0001_initial'),
        ('customers', '0001_initial'),
        ('changers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Identificação')),
                ('document', core.base.fields.CpfField(max_length=14, validators=[core.base.validators.validate_cpf], verbose_name='CPF')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('bench', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='changers.Changer', verbose_name='Cambista')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.Customer', verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'Bilhete',
                'verbose_name_plural': 'Bilhetes',
            },
        ),
        migrations.CreateModel(
            name='TicketOddMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bet_value', models.CharField(max_length=50, verbose_name='Palpite do jogo')),
                ('bet_amount', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='valor da aposta')),
                ('bet_chances', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Valor da cotação')),
                ('is_checked', models.BooleanField(default=False, verbose_name='foi Verificado?')),
                ('is_win', models.BooleanField(default=False, verbose_name='Ganhou?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('odd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='odds.Odd', verbose_name='Cotação')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticketbets', to='tickets.Ticket', verbose_name='Bilhete')),
            ],
            options={
                'verbose_name': 'Aposta',
                'verbose_name_plural': 'Aposta',
            },
        ),
    ]
