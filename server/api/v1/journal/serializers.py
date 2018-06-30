from django.utils.translation import ugettext_lazy as _

from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from apps.journal.models import Journal


class JournalSerializer(ModelSerializer):

    class Meta:
        model = Journal
        fields = [
            'id', 'child', 'time',
            'action', 'parent', 'date'
        ]

    def validate(self, attrs):
        data = super().validate(attrs)
        child = data.get('child') or self.instance.child
        parent = data.get('parent') or self.instance.parent
        if child and parent and not child.parents.filter(id=parent.id).exists():
            raise ValidationError({'parent': _('Указанный родитель не является '
                                               'родителем выбранного ребенка!')})
        return data
