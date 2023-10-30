"""
URL configuration for Reemplazos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
#from django.contrib import admin
from django.urls import path
from django import views

from gestioncurriculum.views import (
    IndexView,
    InicioDeSesionView,
    SubirCurriculumView,
    SolicitudDeReemplazoView,
    ListaDeCandidatosView,
)

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('login/', InicioDeSesionView.as_view(), name='inicio_de_sesion'),
    path('login/emp/', InicioDeSesionView.as_view(), name='inicio_de_sesion_emp'),
    path('registro/', views.registro, name='registro'),
    #path('registro/emp/', RegistroView.as_view(), name='registro_emp'),
    #path('registro/candidatos/', RegistroView.as_view(), name='candidatos'),
    path('upload-curriculum/', SubirCurriculumView.as_view(), name='carga_curriculum'),
    path('request-replacement/', SolicitudDeReemplazoView.as_view(), name='solicitud_de_reemplazo'),
    path('candidates/<int:pk>/', ListaDeCandidatosView.as_view(), name='lista_de_candidatos'),
]


