from shcApp.models.user import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'create_date', 'activo', 'nombre', 'apellido', 'correo', 'direccion', 'telefono', 'rol']

        def create(self, validated_data):
            userInstance = User.objects.create( **validated_data)
            return userInstance