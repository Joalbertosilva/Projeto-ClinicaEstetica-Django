from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),  
    path('promocoes/', views.promocoes, name='promocoes'),
    path('servicos/', views.servicos, name='servicos'),
    path('profissionais/', views.profissionais, name='profissionais'),
    path('agenda/', views.agenda, name='agenda'),
    path('produtos/', views.produtos, name='produtos'),
    path('contato/', views.contato, name='contato'),
    path('produtos-teste/', views.produtos_teste, name='produtos-teste'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_usuario, name='login'),
    path('perfil/', views.perfil_usuario, name='perfil'),
    path('logout/', views.logout_usuario, name='logout'),  
]
