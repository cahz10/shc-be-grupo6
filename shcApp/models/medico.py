from django.db import models
from .user import User
from .auxiliar import Auxiliar

class Medico(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(User, related_name='id_usuario_medico', on_delete=models.CASCADE, unique = True)
    profesion = models.CharField('profesion', max_length = 15)
    eps = models.CharField('eps', max_length = 30)
    nivel = models.IntegerField('nivel', default=0)
    especialidad = models.CharField('especialidad', max_length = 30)
    create_date=models.DateField('create_date')
    registra = models.ForeignKey(Auxiliar, related_name='id_registra_medico', on_delete=models.CASCADE)