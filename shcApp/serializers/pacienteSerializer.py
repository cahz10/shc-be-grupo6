from shcApp.models.paciente import Paciente
from shcApp.models.user import User 
from rest_framework import serializers
from datetime import datetime


class PacienteSerializer(serializers.ModelSerializer):

	class Meta:
		model = Paciente
		fields = ['id', 'eps', 'registra', 'usuario', 'create_date']

	def create(self, validated_data):
		pacienteInstance = Paciente.objects.create(**validated_data)
		return pacienteInstance
		
	def to_representation(self, obj):
		paciente = Paciente.objects.get(id=obj.id)
		user = User.objects.get(id=paciente.usuario.id)
		
		return {
		'Paciente':{
			'id_paciente': paciente.id, 
			'create_date': paciente.create_date,
			'eps': paciente.eps,
			'id_registra_paciente': paciente.registra.id
        },
		'usuario':{
			'id_usuario_auxiliar': user.id,
			'username': user.username,
			'nombre': user.nombre,
			'apellido': user.apellido,
			'create_date': user.create_date,
			'activo':user.activo,
			'correo':user.correo,
			'direccion': user.direccion,
			'telefono':user.telefono,
			'rol':user.rol
		}
	}