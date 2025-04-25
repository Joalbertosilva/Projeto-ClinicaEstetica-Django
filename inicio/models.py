from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UsuarioManager(BaseUserManager):
    def create_user(self, email, senha=None, **extra_fields):  # Alterado de 'password' para 'senha'
        if not email:
            raise ValueError('O email é obrigatório')
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)  # Clientes normais são ativos por padrão
        user = self.model(email=email, **extra_fields)
        user.set_password(senha)  # Usando 'senha' para definir a senha
        user.save(using=self._db)
        return user

    def create_superuser(self, email, senha=None, **extra_fields):  # Alterado de 'password' para 'senha'
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser deve ter is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser deve ter is_superuser=True.')

        return self.create_user(email, senha, **extra_fields)  # Passando 'senha'

class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=255)
    endereco = models.TextField(blank=True, null=True)  # Endereço do cliente
    telefone = models.CharField(max_length=15, blank=True, null=True)  # Telefone do cliente
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)
    imagem_url = models.URLField(max_length=500, blank=True, null=True)
    em_promocao = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


class Agenda(models.Model):
    data = models.DateField()
    hora = models.TimeField()
    profissional = models.ForeignKey('Profissional', on_delete=models.CASCADE)
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.data} - {self.hora}"


class Profissional(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    contato = models.CharField(max_length=15)
    foto = models.ImageField(upload_to='fotos_profissionais/', blank=True, null=True)  # Adicionando imagem para o profissional

    def __str__(self):
        return self.nome


class Servico(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to='fotos_servicos/', blank=True, null=True)  # Adicionando imagem para o serviço

    def __str__(self):
        return self.nome