from django.contrib import admin
from .models import Produto, Usuario, Agenda, Profissional, Servico

admin.site.register(Produto)
admin.site.register(Usuario)
admin.site.register(Agenda)
admin.site.register(Profissional)
admin.site.register(Servico)

