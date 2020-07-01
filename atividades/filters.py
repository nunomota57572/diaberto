import django_filters
from .models import atividade
from utilizador.models import utilizador


class AtividadeFilter(django_filters.FilterSet):
	Nome_actividade = django_filters.CharFilter(lookup_expr='icontains')
	Estado = django_filters.CharFilter(lookup_expr='icontains')
	Criador = django_filters.ModelChoiceFilter(to_field_name='username',queryset=utilizador.objects.all())
	class Meta:
		model = atividade
		fields = ['Nome_actividade', 'Estado', 'Criador']

