# Generated by Django 3.1.5 on 2021-01-31 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id_time', models.IntegerField(primary_key=True, serialize=False)),
                ('nome_time', models.CharField(max_length=80, unique=True)),
                ('id_img', models.IntegerField()),
                ('data_cad', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Time',
                'verbose_name_plural': 'Times',
                'db_table': 'time',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Risco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao_risco', models.CharField(max_length=40)),
                ('valor_risco', models.DecimalField(decimal_places=2, max_digits=9)),
                ('id_time', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='times.time')),
            ],
            options={
                'verbose_name': 'Risco',
                'verbose_name_plural': 'Riscos',
                'db_table': 'risco',
                'managed': True,
            },
        ),
    ]