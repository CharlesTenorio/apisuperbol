# Generated by Django 3.0.3 on 2021-04-21 19:58

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('leagues', '0001_initial'),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True, verbose_name='Evento id')),
                ('sport_id', models.PositiveIntegerField(default=1, verbose_name='Sport')),
                ('time', models.CharField(max_length=200, verbose_name='Timestemp do jogo')),
                ('time_status', models.CharField(choices=[('0', 'Not Started'), ('1', 'InPlay'), ('2', 'TO BE FIXED'), ('3', 'Ended'), ('4', 'Postponed'), ('5', 'Cancelled'), ('6', 'Walkover'), ('7', 'Interrupted'), ('8', 'Abandoned'), ('9', 'Retired'), ('99', 'Removed')], default='0', max_length=50, verbose_name='Tempo atual do jogo')),
                ('ss', models.CharField(blank=True, max_length=50, null=True, verbose_name='Resultado final do jogo')),
                ('scores', django.contrib.postgres.fields.jsonb.JSONField(default=dict, verbose_name='Resultado detalhado')),
                ('stats', django.contrib.postgres.fields.jsonb.JSONField(default=dict, verbose_name='Detalhes da partida')),
                ('events', django.contrib.postgres.fields.jsonb.JSONField(default=dict, verbose_name='Minuto a minuto')),
                ('extra', django.contrib.postgres.fields.jsonb.JSONField(default=dict, verbose_name='Informações adicionais')),
                ('away', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='away_set', to='teams.Team', verbose_name='Fora')),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='home_set', to='teams.Team', verbose_name='Casa')),
                ('league_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leagues.League', verbose_name='Liga')),
            ],
            options={
                'verbose_name': 'Partida',
                'verbose_name_plural': 'Partidas',
            },
        ),
    ]
