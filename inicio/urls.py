from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


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
    path('servicos/<int:servico_id>/profissionais/', views.escolher_profissional, name='escolher-profissionais'),
    path('servicos/<int:servico_id>/profissionais/<int:profissional_id>/horarios/', views.escolher_horario, name='escolher-horario'),
    path('servicos/<int:servico_id>/profissionais/<int:profissional_id>/horarios/<str:data>/<str:hora>/finalizar/', views.finalizar_agendamento, name='finalizar-agendamento'),
    path('agenda/remover/<int:agendamento_id>/', views.remover_agendamento, name='remover_agendamento'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

