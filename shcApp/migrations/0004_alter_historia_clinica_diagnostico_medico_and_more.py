# Generated by Django 4.1.1 on 2022-09-29 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shcApp', '0003_alter_auxiliar_cargo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historia_clinica',
            name='diagnostico_medico',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='sugerencia_cuidado',
            field=models.TextField(),
        ),
    ]
