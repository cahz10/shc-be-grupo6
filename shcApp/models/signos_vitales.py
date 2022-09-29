from django.db import models
from .paciente import Paciente
from .familiar import Familiar
from .medico import Medico

class signosVitales(models.Model):
    id = models.BigAutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, related_name='id_paciente_signosVitales', on_delete=models.CASCADE)
    familiar_registra = models.ForeignKey(Familiar, related_name='id_familiar_signosVitales', on_delete=models.CASCADE, null=True, blank=True)
    medico_consulta = models.ForeignKey(Medico, related_name='id_medico_consulta_signosVitales', on_delete=models.CASCADE, null=True, blank=True)
    oximetria =models.DecimalField('oximetria', max_digits=9, decimal_places=2)
    saturacion = models.DecimalField('saturacion', max_digits=9, decimal_places=2)
    presion = models.DecimalField('presion', max_digits=9, decimal_places=2)
    temperatura = models.DecimalField('temperatura', max_digits=9, decimal_places=2)
    frecuencia_cardiaca = models.DecimalField('frecuencia_cardiaca', max_digits=9, decimal_places=2)
    frecuencia_respiratoria = models.DecimalField('frecuencia_cardiaca', max_digits=9, decimal_places=2)
    glicemia = models.DecimalField('glicemia', max_digits=9, decimal_places=2)
    create_date=models.DateField('create_date')