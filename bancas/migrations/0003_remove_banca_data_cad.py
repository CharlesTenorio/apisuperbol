# Generated by Django 3.1.6 on 2021-02-01 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bancas', '0002_auto_20210131_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banca',
            name='data_cad',
        ),
    ]