from rest_framework.viewsets import ModelViewSet

from apps.journal.models import Journal
from api.v1.journal.filtersets import JournalFilterSet
from api.v1.journal.serializers import JournalSerializer


class JournalViewSet(ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    filter_class = JournalFilterSet
