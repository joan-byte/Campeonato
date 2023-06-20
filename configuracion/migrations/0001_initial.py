# Generated by Django 4.2.2 on 2023-06-20 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='caracteristicas_campeonato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_campeonato', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='tournament_logos/')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('lugar', models.CharField(max_length=50)),
                ('num_partidas', models.IntegerField()),
                ('serieB', models.BooleanField(default=False)),
                ('puntos_totales', models.BooleanField(default=False)),
            ],
        ),
    ]
