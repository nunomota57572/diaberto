import django_filters
from .models import Notificacao
from utilizador.models import utilizador


class NotificacaoFilter(django_filters.FilterSet):
	SUPERUSER_CHOICES = {
        ('', 'Todas'),
        ('True', 'Lida'),
        ('False', 'Não Lida')
    }
	assunto = django_filters.CharFilter(lookup_expr='icontains')
	is_read = django_filters.ChoiceFilter(lookup_expr='exact',choices=SUPERUSER_CHOICES, empty_label=None)
	autorid = django_filters.ModelChoiceFilter(to_field_name='username',queryset=utilizador.objects.all())
	
	
	class Meta:
		model = Notificacao
		fields = ['assunto', 'is_read', 'autorid']

