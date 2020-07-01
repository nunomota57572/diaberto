import django_filters
from .models import disponibilidade, tarefa
from utilizador.models import colab, coord
from configuracoes.models import dias_DA

class TarefaFilter(django_filters.FilterSet):
	Nome = django_filters.CharFilter(lookup_expr='icontains')
	Tipo = django_filters.CharFilter(lookup_expr='icontains')
	Concluida = django_filters.CharFilter(lookup_expr='icontains')
	UtilizadorID2 = django_filters.ModelChoiceFilter(to_field_name='username',queryset=colab.objects.all())

	class Meta:
		model = tarefa
		fields = ['Nome', 'Tipo', 'Concluida','UtilizadorID2']

class DisponibilidadeFilter(django_filters.FilterSet):
	Dia = django_filters.ModelChoiceFilter(field_name='Dia',queryset=dias_DA.objects.all())
	Inicio = django_filters.CharFilter(lookup_expr='icontains')
	Fim = django_filters.CharFilter(lookup_expr='icontains')
	class Meta:
		model = disponibilidade
		fields = ['Dia', 'Inicio', 'Fim', 'Observacoes']


class ColabFilter(django_filters.FilterSet):
	username = django_filters.CharFilter(lookup_expr='icontains')
	first_name = django_filters.CharFilter(lookup_expr='icontains')
	last_name = django_filters.CharFilter(lookup_expr='icontains')
	# UO = django_filters.CharFilter(lookup_expr='icontains')
	class Meta:
		model = colab
		fields = ['username', 'first_name', 'last_name']
