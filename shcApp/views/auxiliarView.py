from datetime import datetime
from django.conf import settings
from shcApp.models import User, Auxiliar
from rest_framework import status, views, generics
from rest_framework.response import Response
from shcApp.serializers import UserSerializer, AuxiliarSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.backends import TokenBackend


class AuxiliarView(views.APIView):

    def post(self, request, *args, **kwargs):
        data_usuario = request.data.pop('usuario_info')
        now = datetime.now()
        data_usuario['create_date'] =now.strftime("%Y-%m-%d")
        data_usuario['rol'] = User.AplicationRol.AUX
        serializer_user = UserSerializer(data = data_usuario)
        serializer_user.is_valid(raise_exception=True)
        usuario = serializer_user.save()

        data_auxiliar = request.data.pop('auxiliar_info')
        data_auxiliar['usuario'] = usuario.id
        data_auxiliar['create_date'] =now.strftime("%Y-%m-%d")
        serializer_auxiliar = AuxiliarSerializer(data = data_auxiliar)
        serializer_auxiliar.is_valid(raise_exception=True)
        auxiliar = serializer_auxiliar.save()

        tokenData = {"username":data_usuario["username"],
                    "password":data_usuario["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        return_data = {"auxiliar": AuxiliarSerializer(auxiliar).data,
                        "token_data" : tokenSerializer.validated_data}
        return Response(return_data, status = status.HTTP_201_CREATED)

    def delete (self, request, *args, **kwargs):
        auxiliar = Auxiliar.objects.filter(id = kwargs['pk']).first()
        usuario = User.objects.filter(id = auxiliar.usuario.id).first()

        auxiliar.delete()
        usuario.delete()

        stringResponse = {'detail': 'Registro eliminado exitosamente'}	

        return Response(stringResponse, status = status.HTTP_200_OK)
		
    def get(self, request, *args, **kwargs):
            try:
                token = request.META.get('HTTP_AUTHORIZATION')[7:]
                tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
                valid_data = tokenBackend.decode(token,verify=False)
                auxiliar = Auxiliar.objects.get(id = kwargs['pk'])
                if valid_data['user_id'] != auxiliar.usuario.id:
                    stringResponse = {'detail':'Unauthorized Request'}
                    return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
            
            except:
                stringResponse = {'detail':'No hay token'}
                return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
                    
            serializer_aux = AuxiliarSerializer (auxiliar)
            return Response(serializer_aux.data, status = status.HTTP_200_OK)
                
    def put (self, request, *args, **kwargs):
        auxiliar = Auxiliar.objects.get(id = kwargs['pk'])
        usuario = User.objects.get(id = auxiliar.usuario.id)
        now = datetime.now()
        
        data_usuario = request.data.pop('usuario_info')
        data_usuario['create_date'] =now.strftime("%Y-%m-%d")
        #data_auxiliar['usuario'] = usuario.id
        
        serializer_user = UserSerializer(data = data_usuario)
        serializer_user.is_valid(raise_exception=True)                   
        usuario = serializer_user.save()                        

        data_auxiliar = request.data.pop('auxiliar_info')
        data_auxiliar['create_date'] =now.strftime("%Y-%m-%d")
        
        serializer_auxiliar = AuxiliarSerializer(auxiliar,data = data_auxiliar)
        serializer_auxiliar.is_valid(raise_exception=True)
        auxiliar = serializer_auxiliar.save() 
        
        return_data = {'auxiliar': AuxiliarSerializer(auxiliar).data}
        return Response(return_data, status = status.HTTP_200_OK)
		
class AllAuxiliares(generics.ListAPIView):
		queryset = Auxiliar.objects.all()
		serializer_class =AuxiliarSerializer
		

		def list (self, request):
		
			queryset = self.get_queryset()
			serializer = AuxiliarSerializer(queryset, many=True)
			
			return Response(serializer.data, status = status.HTTP_200_OK)