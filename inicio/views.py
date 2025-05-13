from django.shortcuts import render, redirect
from decimal import Decimal
from django.contrib.auth import authenticate, login
from .models import Usuario, Profissional, Servico, Agenda, Produto
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime, timedelta, time
from django.shortcuts import get_object_or_404
from inicio.forms import UsuarioFormulario

def index(request):
    produtos_promocao = Produto.objects.filter(em_promocao=True)

    for produto in produtos_promocao:
        produto.preco_com_desconto = Decimal(produto.preco) * Decimal(0.6)  # Garantir precisão de decimais

    return render(request, 'inicio/index.html', {'produtos': produtos_promocao})


def cadastro(request):
    if request.method == 'POST':
        form = UsuarioFormulario(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Usuario.objects.filter(email=email).exists():
                messages.error(request, 'Já existe um usuário com este e-mail.')
            else:
                usuario = form.save(commit=False)
                senha = form.cleaned_data['senha']
                usuario.set_password(senha)  
                usuario.save()
                messages.success(request, 'Cadastro realizado com sucesso!')
                return redirect('login')
        else:
            messages.error(request, 'Erro ao realizar cadastro.')
    else:
        form = UsuarioFormulario()

    return render(request, 'inicio/cadastro.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        
        usuario = authenticate(request, username=email, password=senha)
        if usuario is not None:
            login(request, usuario)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('index')  
        else:
            messages.error(request, 'Credenciais inválidas')
            return redirect('login')

    return render(request, 'inicio/login.html')


@login_required
def perfil_usuario(request):
    if request.method == 'POST':
        foto_perfil = request.FILES.get('foto_perfil')
        if foto_perfil:
            request.user.foto_perfil = foto_perfil
            request.user.save()
            messages.success(request, 'Foto de perfil atualizada com sucesso!')

    return render(request, 'inicio/perfil.html', {'usuario': request.user})



def logout_usuario(request):
    list(messages.get_messages(request))
    logout(request)
    return redirect('index')  

def promocoes(request):
    return render(request, 'inicio/promocoes.html')

def servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'inicio/servicos.html', {'servicos': servicos})

def profissionais(request):
    lista_profissionais = Profissional.objects.all()  # Busca todos os profissionais
    return render(request, 'inicio/profissionais.html', {'profissionais': lista_profissionais})

def escolher_profissional(request, servico_id):
    servico = Servico.objects.get(id=servico_id)
    profissionais = Profissional.objects.all()
    return render(request, 'inicio/escolher-profissionais.html', {'servico': servico, 'profissionais': profissionais})

def escolher_horario(request, servico_id, profissional_id):
    servico = Servico.objects.get(id=servico_id)
    profissional = Profissional.objects.get(id=profissional_id)

    # Obter os agendamentos existentes para o profissional
    agendamentos = Agenda.objects.filter(profissional=profissional)

    # Gerar horários disponíveis (segunda a sábado, manhã e tarde)
    horarios_disponiveis = []
    dias_da_semana = [0, 1, 2, 3, 4, 5]  # Segunda a sábado
    horarios = [
        time(8, 0), time(9, 0), time(10, 0), time(11, 0),  # Manhã
        time(14, 0), time(15, 0), time(16, 0), time(17, 0)  # Tarde
    ]

    for i in range(7):  # Próximos 7 dias
        dia = datetime.now().date() + timedelta(days=i)
        if dia.weekday() in dias_da_semana:  # Verifica se é de segunda a sábado
            for hora in horarios:
                # Verifica se o horário já está ocupado
                if not agendamentos.filter(data=dia, hora=hora).exists():
                    horarios_disponiveis.append({'data': dia, 'hora': hora})

    return render(request, 'inicio/escolher-horario.html', {
        'servico': servico,
        'profissional': profissional,
        'horarios_disponiveis': horarios_disponiveis
    })
def finalizar_agendamento(request, servico_id, profissional_id, data, hora):
    if request.method == 'POST':
        servico = Servico.objects.get(id=servico_id)
        profissional = Profissional.objects.get(id=profissional_id)
        cliente = request.user

        # Criar o agendamento
        Agenda.objects.create(
            data=data,
            hora=hora,
            profissional=profissional,
            cliente=cliente
        )

        return redirect('perfil')  # Redireciona para o perfil do usuário

    return render(request, 'inicio/finalizar-agendamento.html', {
        'servico': Servico.objects.get(id=servico_id),
        'profissional': Profissional.objects.get(id=profissional_id),
        'data': data,
        'hora': hora
    })

def agenda(request):
    return render(request, 'inicio/agenda.html')

@login_required
def agenda(request):
    usuario = request.user
    agendamentos = Agenda.objects.filter(cliente=usuario)  # Filtra os agendamentos do usuário logado
    return render(request, 'inicio/agenda.html', {'agendamentos': agendamentos})

@login_required
def remover_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agenda, id=agendamento_id, cliente=request.user)
    agendamento.delete()
    return redirect('agenda')  # Redireciona para a página de agendamentos

def produtos(request):
    lista_produtos = Produto.objects.all()
    return render(request, 'inicio/produtos.html', {'produtos': lista_produtos})

def contato(request):
    return render(request, 'inicio/contato.html')

def produtos_teste(request):
    lista_produtos = Produto.objects.all()
    return render(request, 'inicio/produtos.html', {'produtos': lista_produtos})

