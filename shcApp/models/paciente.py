from django.db import models
from .user import User
from .auxiliar import Auxiliar

class Paciente(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(User, related_name='id_usuario_Paciente', on_delete=models.CASCADE, unique=True)
    eps = models.CharField('eps', max_length = 30)
    create_date=models.DateField('create_date')
    registra = models.ForeignKey(Auxiliar, related_name='id_registra_paciente', on_delete=models.CASCADE)