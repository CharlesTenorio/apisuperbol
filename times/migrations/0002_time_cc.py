# Generated by Django 3.1.6 on 2021-02-01 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('times', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='time',
            name='cc',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
