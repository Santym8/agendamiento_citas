# Generated by Django 4.0.5 on 2022-06-26 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
        ('medicos', '0007_alter_truno_medico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truno',
            name='paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pacientes.paciente'),
        ),
    ]
