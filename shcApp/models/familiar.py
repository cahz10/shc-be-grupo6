from django.db import models
from .user import User
from .auxiliar import Auxiliar

class Familiar(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(User, related_name='id_usuario_familiar', on_delete=models.CASCADE, unique = True)
    create_date=models.DateField('create_date')
    registra = models.ForeignKey(Auxiliar, related_name='id_registra_familiar', on_delete=models.CASCADE)