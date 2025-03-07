from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),  # Página inicial
    path('promocoes/', views.promocoes, name='promocoes'),
    path('servicos/', views.servicos, name='servicos'),
    path('profissionais/', views.profissionais, name='profissionais'),
    path('agenda/', views.agenda, name='agenda'),
    path('produtos/', views.produtos, name='produtos'),
    path('contato/', views.contato, name='contato'),
]
