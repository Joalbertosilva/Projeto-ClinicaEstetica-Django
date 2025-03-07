from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),  # Rota da página principal
    path('contas/', include('contas.urls')),  # Rotas de login/cadastro
]
