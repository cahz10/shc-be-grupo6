from datetime import datetime
from shcApp.models import User, Auxiliar
from rest_framework import status, views
from rest_framework.response import Response
from shcApp.serializers import UserSerializer, AuxiliarSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class AuxiliarView(views.APIView):

    def post(self,request, *args, **kwargs):
        data_usuario = request.data.pop('usuario_info')
        now = datetime.now()
        data_usuario['create_date'] =now.strftime("%Y-%m-%d")
        data_usuario['rol'] = User.AplicationRol.AUX
        serializer_user = UserSerializer(data = data_usuario)
        serializer_user.is_valid(raise_exception=True)
        usuario = serializer_user.save

        data_auxiliar = request.data.pop('auxiliar_info')
        data_auxiliar['usuario'] = usuario.id
        data_auxiliar['create_date'] =now.strftime("%Y-%m-%d")
        serializer_auxiliar = AuxiliarSerializer(data = data_auxiliar)
        serializer_auxiliar.is_valid(raise_exception=True)
        auxiliar = serializer_auxiliar.save

        tokenData = {"username":request.data["username"],
        "password":request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        return_data = {"auxiliar": AuxiliarSerializer(auxiliar).data,
                        "token_data" : tokenSerializer.validated_data}
        return Response(return_data, status = status.HTTP_201_CREATED)