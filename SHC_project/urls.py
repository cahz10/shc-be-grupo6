"""SHC_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from shcApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registrarAuxiliar/', views.AuxiliarView.as_view()),
    path('eliminarAuxiliar/<int:pk>', views.AuxiliarView.as_view()),
	path('actualizarAuxiliar/<int:pk>', views.AuxiliarView.as_view()),
	path('consultarAuxiliar/<int:pk>', views.AuxiliarView.as_view()),
	path('consultarAllAuxiliar/', views.AllAuxiliares.as_view()),
    path('registrarPaciente/', views.PacienteView.as_view()),
    path('eliminarPaciente/<int:pk>/<int:id_usuario_accion>', views.PacienteView.as_view()),
    path('consultarPaciente/<int:pk>/<int:id_usuario_accion>', views.PacienteView.as_view()),
	path('consultarAllPacientes/<int:id_usuario_accion>', views.AllPacientes.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    
]
