import django_filters

from .models import utilizador
from configuracoes.models import uos, departamentos, cursos

class UtilizadorFilter(django_filters.FilterSet):
	username = django_filters.CharFilter(lookup_expr='icontains')
	UO = django_filters.ModelChoiceFilter(to_field_name='sigla', queryset=uos.objects.all())
	Departamento = django_filters.ModelChoiceFilter(to_field_name='departamento', queryset=departamentos.objects.all())
	Curso = django_filters.ModelChoiceFilter(to_field_name='sigla', queryset=cursos.objects.all())

	class Meta:
		model = utilizador
		fields = ['username', 'UO', 'Departamento', 'Curso']
