from django.db import models
from .paciente import Paciente
from .medico import Medico
from .auxiliar import Auxiliar

class Medico_Paciente(models.Model):
    id = models.BigAutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, related_name='id_paciente_medico_medicoPaciente', on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, related_name='id_medico', on_delete=models.CASCADE)  
    fecha_inicio = models.DateField('fecha_inicio')
    fecha_fin = models.DateField('fecha_fin')
    registra = models.ForeignKey(Auxiliar, related_name='id_registra_medico_paciente', on_delete=models.CASCADE)