# Generated by Django 2.2.3 on 2019-07-26 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('municipios', models.ManyToManyField(blank=True, to='Ciudad.Municipio')),
            ],
        ),
    ]
