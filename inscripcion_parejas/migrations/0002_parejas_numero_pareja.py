# Generated by Django 4.2.2 on 2023-06-29 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion_parejas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parejas',
            name='Numero_pareja',
            field=models.IntegerField(default=0),
        ),
    ]