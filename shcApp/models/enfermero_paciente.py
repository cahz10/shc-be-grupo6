from django.db import models
from .paciente import Paciente
from .enfermero import Enfermero
from .auxiliar import Auxiliar

class Enfermero_Paciente(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_paciente = models.ForeignKey(Paciente, related_name='id_paciente_enfermeropaciente', on_delete=models.CASCADE, unique = True)
    id_enfermero = models.ForeignKey(Enfermero, related_name='id_enfermero_enfermeropaciente', on_delete=models.CASCADE, unique = True)  
    fecha_inicio = models.DateField('fecha_inicio')
    fecha_fin = models.DateField('fecha_fin')
    id_registra = models.ForeignKey(Auxiliar, related_name='id_registra_enfermero_paciente', on_delete=models.CASCADE)