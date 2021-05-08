# Generated by Django 3.0.3 on 2021-04-21 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('match', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Odd',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('event_id', models.CharField(max_length=255, verbose_name='Evento id')),
                ('market', models.CharField(choices=[('1_1\t', ' 1X2, Full Time Result'), ('1_2\t', ' Asian Handicap'), ('1_3\t', ' O/U, Goal Line'), ('1_4\t', ' Asian Corners'), ('1_5\t', ' 1st Half Asian Handicap'), ('1_6\t', ' 1st Half Goal Line'), ('1_7\t', ' 1st Half Asian Corners\t1_8\tHalf Time Result'), ('18_1', 'Money Line'), ('18_2', 'Spread'), ('18_3', 'Total Points'), ('18_4', 'Money Line (Half)'), ('18_5', 'Spread (Half)'), ('18_6', 'Total Points (Half)'), ('18_7', 'Quarter - Winner (2-Way)'), ('18_8', 'Quarter - Handicap'), ('18_9', 'Quarter - Total (2-Way)'), ('*_1\t', ' Match Winner 2-Way'), ('*_2\t', ' Asian Handicap'), ('*_3\t', ' Over/Under'), ('3_4\t', ' Draw No Bet (Cricket)')], max_length=50, verbose_name='Market Key')),
                ('source', models.CharField(default='bet365', max_length=50, verbose_name='Api name')),
                ('description', models.CharField(blank=True, max_length=150, null=True, verbose_name='Descrição')),
                ('first_od', models.CharField(choices=[('home_od', 'Casa'), ('draw_od', 'Empate'), ('away_od', 'Fora'), ('over_od', 'Vê com zé'), ('handicap', 'Escanteios'), ('under_od', 'Não sei')], max_length=50, verbose_name='Label 1')),
                ('first_od_value', models.CharField(max_length=50, verbose_name='Valor 1')),
                ('second_od', models.CharField(choices=[('home_od', 'Casa'), ('draw_od', 'Empate'), ('away_od', 'Fora'), ('over_od', 'Vê com zé'), ('handicap', 'Escanteios'), ('under_od', 'Não sei')], max_length=50, verbose_name='Label 2')),
                ('second_od_value', models.CharField(max_length=50, verbose_name='Valor 2')),
                ('last_od', models.CharField(max_length=50, verbose_name='Label 3')),
                ('last_od_value', models.CharField(choices=[('home_od', 'Casa'), ('draw_od', 'Empate'), ('away_od', 'Fora'), ('over_od', 'Vê com zé'), ('handicap', 'Escanteios'), ('under_od', 'Não sei')], max_length=50, verbose_name='Valor 3')),
                ('ss', models.CharField(blank=True, max_length=50, null=True, verbose_name='Resultado final do jogo')),
                ('time_str', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tempo atual do jogo')),
                ('add_time', models.CharField(max_length=100, verbose_name='Timestemp do momento da cotação')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='match.Match', verbose_name='Jogo')),
            ],
            options={
                'verbose_name': 'Cotação',
                'verbose_name_plural': 'Cotações',
            },
        ),
    ]
