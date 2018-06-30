from django.utils.translation import ugettext_lazy as _

from django_filters import FilterSet, BooleanFilter

from apps.journal.models import Journal


class JournalFilterSet(FilterSet):
    is_studying = BooleanFilter(
        field_name='child__is_studying',
        help_text=_('Введите True, если ребенок учится, '
                    'или False, если не учится')
    )

    class Meta:
        model = Journal
        fields = ['child', 'action']
