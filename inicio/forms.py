from django import forms
from .models import Usuario

class UsuarioFormulario(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput, label='Senha')  

    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'endereco', 'telefone', 'senha']
        widgets = {
            'endereco': forms.Textarea(attrs={'rows': 3, 'cols': 40}),  
        }

class LoginFormulario(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
