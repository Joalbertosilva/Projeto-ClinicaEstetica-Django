from django.shortcuts import render
from .models import Produto

def index(request):
    return render(request, 'inicio/index.html')

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