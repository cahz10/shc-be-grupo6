from django.db import models
from .paciente import Paciente
from .medico import Medico
from .familiar import Familiar

class Historia_Clinica(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_paciente = models.ForeignKey(Paciente, related_name='id_paciente_historiaClinica', on_delete=models.CASCADE)
    familiar_consulta = models.ForeignKey(Familiar, related_name='id_familiar_consulta', on_delete=models.CASCADE, null=True, blank=True)
    medico = models.ForeignKey(Medico, related_name='medico_historiaClinica', on_delete=models.CASCADE, null=True, blank=True)
    diagnostico_medico = models.TextField()
    sugerencia_cuidado = models.TextField()  
    create_date = models.DateField('create_date')