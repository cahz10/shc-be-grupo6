from django.db import models
from .paciente import Paciente
from .familiar import Familiar
from .auxiliar import Auxiliar

class Familiar_Paciente(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_paciente = models.ForeignKey(Paciente, related_name='id_paciente_familiarPaciente', on_delete=models.CASCADE)
    id_familiar = models.ForeignKey(Familiar, related_name='id_familiar_familiarPaciente', on_delete=models.CASCADE)  
    fecha_inicio = models.DateField('fecha_inicio')
    fecha_fin = models.DateField('fecha_fin')
    id_registra = models.ForeignKey(Auxiliar, related_name='id_registra_familiar_paciente', on_delete=models.CASCADE)