from django.db import models
from .user import User

class Auxiliar(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(User, related_name='id_usuario_auxiliar', on_delete=models.CASCADE, unique=True)
    cargo = models.CharField('cargo', max_length = 100)    
    create_date=models.DateField('create_date')