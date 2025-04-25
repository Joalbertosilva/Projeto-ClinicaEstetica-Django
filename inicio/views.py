from django.shortcuts import render, redirect
from .models import Produto
from decimal import Decimal
from django.contrib.auth import authenticate, login
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index(request):
    produtos_promocao = Produto.objects.filter(em_promocao=True)

    for produto in produtos_promocao:
        produto.preco_com_desconto = Decimal(produto.preco) * Decimal(0.6)  # Garantir precisão de decimais

    return render(request, 'inicio/index.html', {'produtos': produtos_promocao})


def cadastro(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        senha_confirmada = request.POST.get('senha_confirmada')

        if Usuario.objects.filter(email=email).exists():
            return render(request, 'inicio/cadastro.html', {
                'error_message': 'Este email já está em uso. Tente outro.'
            })

        if len(senha) < 8:
            return render(request, 'inicio/cadastro.html', {
                'error_message': 'A senha deve conter pelo menos 8 caracteres.'
            })

        if senha != senha_confirmada:
            return render(request, 'inicio/cadastro.html', {
                'error_message': 'As senhas não coincidem. Tente novamente.'
            })

        try:
            usuario = Usuario.objects.create_user(email=email, nome=nome, senha=senha)
            return render(request, 'inicio/cadastro.html', {
                'success_message': 'Usuário cadastrado com sucesso!'
            })
        except IntegrityError:
            return render(request, 'inicio/cadastro.html', {
                'error_message': 'Erro ao cadastrar o usuário. Tente novamente.'
            })

    return render(request, 'inicio/cadastro.html')

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
    return render(request, 'inicio/servicos.html')

def profissionais(request):
    return render(request, 'inicio/profissionais.html')

def agenda(request):
    return render(request, 'inicio/agenda.html')

def produtos(request):
    lista_produtos = Produto.objects.all()
    return render(request, 'inicio/produtos.html', {'produtos': lista_produtos})

def contato(request):
    return render(request, 'inicio/contato.html')

def produtos_teste(request):
    lista_produtos = Produto.objects.all()
    return render(request, 'inicio/produtos.html', {'produtos': lista_produtos})

