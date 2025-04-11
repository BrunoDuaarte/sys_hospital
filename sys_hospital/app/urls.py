from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pacientes.views import PacienteViewSet  # Importando a ViewSet de Paciente
from enderecos.views import EnderecoViewSet  # Se existir um ViewSet para Endereços

# Criando um roteador e registrando os ViewSets
router = DefaultRouter()
router.register(r'pacientes', PacienteViewSet)
router.register(r'enderecos', EnderecoViewSet)  # Se necessário

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Aqui agora o router está definido corretamente
]

