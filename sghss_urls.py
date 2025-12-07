from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pacientes.views import PacienteViewSet
from consultas.views import ConsultaViewSet
from usuarios.urls_auth import urlpatterns as auth_urls
from usuarios.urls import urlpatterns as usuarios_urls

router = DefaultRouter()
router.register(r'pacientes', PacienteViewSet, basename='paciente')
router.register(r'consultas', ConsultaViewSet, basename='consulta')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include((auth_urls, 'auth'))),
    path('api/', include(router.urls)),
    path('api/', include((usuarios_urls, 'usuarios'))),
]
