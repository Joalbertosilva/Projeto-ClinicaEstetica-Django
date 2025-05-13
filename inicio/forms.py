from django import forms
from .models import Usuario

class UsuarioFormulario(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput, label='Senha')  # Campo para senha

    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'endereco', 'telefone', 'senha']
        widgets = {
            'endereco': forms.Textarea(attrs={'rows': 3, 'cols': 40}),  # Ajusta o tamanho do textarea
        }