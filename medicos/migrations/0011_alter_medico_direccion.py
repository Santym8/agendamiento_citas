# Generated by Django 4.0.5 on 2022-07-07 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0010_medico_direccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='direccion',
            field=models.CharField(max_length=50, verbose_name='Direccion'),
        ),
    ]