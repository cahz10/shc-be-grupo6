from datetime import datetime
from shcApp.models import User, Auxiliar
from rest_framework import status, views, generics
from shcApp.models.medico import Medico
from shcApp.models.paciente import Paciente
from shcApp.serializers import UserSerializer, AuxiliarSerializer, PacienteSerializer
from django.conf import settings
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

def validatePaciente(request, **kwargs):
	token = request.META.get('HTTP_AUTHORIZATION')[7:]	
	tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
	valid_data = tokenBackend.decode(token, verify=False)
	paciente = Paciente.objects.get(id = kwargs['pk'])
	paciente_no_valido = paciente.usuario.id != valid_data['user_id']
	return paciente_no_valido
  

def validateAuxBody(request, **kwargs):
	token = request.META.get('HTTP_AUTHORIZATION')[7:]	
	tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
	valid_data = tokenBackend.decode(token, verify=False)
	aux_registra = Auxiliar.objects.get(id = request.data['paciente_info']['registra'])
	usuario_auxiliar = User.objects.get(id = aux_registra.usuario.id)
	tokenNoValido = aux_registra == None or valid_data['user_id'] != aux_registra.usuario.id or usuario_auxiliar.rol  != User.AplicationRol.AUX  
	return tokenNoValido

def validateTokenAuxUrl(request, **kwargs):
	token = request.META.get('HTTP_AUTHORIZATION')[7:]	
	tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
	valid_data = tokenBackend.decode(token, verify=False)
	aux_registra = Auxiliar.objects.get(id = kwargs['id_usuario_accion'])
	usuario_auxiliar = User.objects.get(id = aux_registra.usuario.id)
	tokenNoValido = aux_registra == None or valid_data['user_id'] != aux_registra.usuario.id or usuario_auxiliar.rol != User.AplicationRol.AUX  
	return tokenNoValido

def validateMedico(token, id_medico):
	try:
		tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
		valid_data = tokenBackend.decode(token, verify=False)
		medico = Medico.objects.get(id = id_medico)
		usuario = User.objects.get(id = medico.usuario.id)
		auxiliar_no_valido = valid_data['user_id'] != medico.usuario.id or usuario.rol !=User.AplicationRol.MED
		return auxiliar_no_valido
	except:
		return True
		

class PacienteView(views.APIView):

    def post(self, request, *args, **kwargs):
        try:
            tokenNoValido = validateAuxBody(request, **kwargs)

        except:
            stringResponse = {'detail':'No hay token'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        if tokenNoValido:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status = status.HTTP_401_UNAUTHORIZED)
		
#se guarda usuario
			
        data_usuario = request.data.pop('usuario_info')
        now = datetime.now()
        data_usuario['create_date'] =now.strftime("%Y-%m-%d")
        data_usuario['rol'] = User.AplicationRol.PAC
        serializer_user = UserSerializer(data = data_usuario)
        serializer_user.is_valid(raise_exception=True)
        usuario = serializer_user.save() 
		
		
#se crea paciente	

        data_paciente = request.data.pop('paciente_info')
        data_paciente['usuario'] = usuario.id
        data_paciente['create_date'] = now.strftime("%Y-%m-%d")   
        serializer_paciente = PacienteSerializer(data = data_paciente)
        serializer_paciente.is_valid(raise_exception=True)
        paciente = serializer_paciente.save()                               
		
        tokenData = {"username":data_usuario['username'],             
        "password":data_usuario['password']}							 
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        return_data = {"paciente": PacienteSerializer(paciente).data,   
				"token_data" : tokenSerializer.validated_data}
        return Response(return_data, status = status.HTTP_201_CREATED)

		
    def delete(self, request, *args, **kwargs):
    
        try:
            pacienteNoValido = validatePaciente(request, **kwargs) 	
            if pacienteNoValido:
                auxiliarNoValido = validateTokenAuxUrl(request, **kwargs) 
            else:
                auxiliarNoValido=False
            
        except:
            stringResponse = {'detail':'No hay token'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        if auxiliarNoValido and pacienteNoValido:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status = status.HTTP_401_UNAUTHORIZED)
                
        paciente = Paciente.objects.filter(id = kwargs['pk']).first()   #95
        usuario = User.objects.filter(id = paciente.usuario.id).first()
            
        paciente.delete()
        usuario.delete()
            
        stringResponse = {'detail': 'Registro eliminado exitosamente'}	
            
        return Response(stringResponse, status = status.HTTP_200_OK)
        
    def get(self, request, *args, **kwargs):
    
        try:
            pacienteNoValido = validatePaciente(request, **kwargs) 	
            if pacienteNoValido:
                auxiliarNoValido = validateTokenAuxUrl(request, **kwargs) 
            else:
                auxiliarNoValido=False
            
        except:
            stringResponse = {'detail':'No hay token'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        if auxiliarNoValido and pacienteNoValido:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status = status.HTTP_401_UNAUTHORIZED)
                
        paciente = Paciente.objects.get(id = kwargs['pk'])
        serializer_aux = PacienteSerializer(paciente)
        return Response(serializer_aux.data, status = status.HTTP_200_OK)
			
		
    def put(self, request, *args, **kwargs):
    
        try:
            pacienteNoValido = validatePaciente(request, **kwargs) 	
            if pacienteNoValido:
                auxiliarNoValido = validateTokenAuxUrl(request, **kwargs) 
            else:
                auxiliarNoValido=False
            
        except:
            stringResponse = {'detail':'No hay token'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        if auxiliarNoValido and pacienteNoValido:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status = status.HTTP_401_UNAUTHORIZED)
            
        paciente = Paciente.objects.get(id = kwargs['pk'])
        usuario = User.objects.get(id = paciente.usuario.id)
        now = datetime.now()
            
        data_usuario = request.data.pop('usuario_info')
        data_usuario['create_date'] =now.strftime("%Y-%m-%d")
        serializer_user = UserSerializer(usuario, data = data_usuario)
        serializer_user.is_valid(raise_exception=True)
        usuario = serializer_user.save() 

        data_paciente = request.data.pop('paciente_info')
        data_paciente['create_date'] = now.strftime("%Y-%m-%d")
        serializer_paciente = PacienteSerializer(paciente, data = data_paciente)
        serializer_paciente.is_valid(raise_exception=True)
        paciente = serializer_paciente.save() 
            
        return_data = {'paciente': PacienteSerializer(paciente).data}
        return Response(return_data, status = status.HTTP_200_OK)   
    
		
class AllPacientes(generics.ListAPIView):
	queryset = Paciente.objects.all()
	serializer_class = PacienteSerializer
		
	def list(self, request, **kwargs):
		auxiliarNoValido = True
		medicoNoValido = True
		
		try:
			token = request.META.get('HTTP_AUTHORIZATION')[7:]		
			auxiliarNoValido = validateAuxBody(token, kwargs['id_usuario_accion'])
			medicoNoValido = validateMedico(token, kwargs['id_usuario_accion'])
			
		except:
			stringResponse = {'detail': 'No hay token valido'}
			return Response(stringResponse, status = status.HTTP_401_UNAUTHORIZED)
			
		if auxiliarNoValido and medicoNoValido:
			stringResponse = {'detail': 'Unauthorized Request'}
			return Response(stringResponse, status = status.HTTP_401_UNAUTHORIZED)
			
		queryset = self.get_queryset()
		print(kwargs['id_usuario_accion'])
		serializer = PacienteSerializer(queryset, many=True)
		return Response(serializer.data, status = status.HTTP_200_OK)
