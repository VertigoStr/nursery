from rest_framework.serializers import ModelSerializer

from apps.journal.models import Journal


class JournalSerializer(ModelSerializer):

    class Meta:
        model = Journal
        fields = [
            'id', 'child', 'time',
            'action', 'parent', 'date'
        ]
