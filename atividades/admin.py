from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import atividade



fieldsets = [
    ("Nome", {'fields': ["Nome"]}),
    ("Submetido", {'fields': ["Submetido"]}),
    ("Criador", {'fields': ["Criador"]}),
    ("Estado", {"fields": ["Estado"]}),
    ("Tipodeatividade", {'fields': ["Tipodeatividade"]}),
    ("Descrição", {'fields': ["Descrição"]}),
    ("Campus", {'fields': ["Campus"]}),
    ("EntidadeOrganizacional", {'fields': ["EntidadeOrganizacional"]}),
    ("Departamento", {"fields": ["Departamento"]})
]

formfield_overrides = {
    models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
}

admin.site.register(atividade)
