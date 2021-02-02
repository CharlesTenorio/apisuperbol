# Generated by Django 3.1.5 on 2021-01-31 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apostas', '0008_aposta_data_aposta'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aposta',
            options={'managed': True, 'verbose_name': 'Aposta', 'verbose_name_plural': 'Apostas'},
        ),
        migrations.AddField(
            model_name='aposta',
            name='cotacao',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aposta',
            name='ganhou',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='aposta',
            name='possivel_retorno',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aposta',
            name='qtd_jogos',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='aposta',
            name='total_apostado',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='aposta',
            table='aposta',
        ),
    ]
