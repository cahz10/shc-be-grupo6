from shcApp.models.user import User
from shcApp.models.auxiliar import Auxiliar
from rest_framework import serializers


class AuxiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auxiliar
        fields = ['id', 'cargo', 'usuario', 'create_date']

    def create(self, validate_data):
        auxiliarInstance = Auxiliar.objects.create(**validate_data)
        return auxiliarInstance

    def to_representation(self, obj):
        auxiliar = Auxiliar.objects.get(id=obj.id)
        user = User.objects.get(id=auxiliar.usuario.id)

        return {
            'auxiliar':{
                'id_auxiliar' : auxiliar.id,
                'create_date' : auxiliar.create_date,
                'cargo' : auxiliar.cargo
            },
            'usuario' : {
                'id_usuario' : user.id,
                'username' : user.username,
                'password' : user.password,
                'create_date' : user.create_date,
                'activo' : user.activo,
                'nombre' : user.nombre,
                'apellido' : user.apellido,               
                'correo' : user.correo,
                'direccion' : user.direccion,
                'telefono' : user.telefono,
                'rol' : user.rol
            }
        }