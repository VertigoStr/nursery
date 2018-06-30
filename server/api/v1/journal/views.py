from apps.journal.models import Journal

from api.common import ListCreateAPIViewSet
from api.v1.journal.filtersets import JournalFilterSet
from api.v1.journal.serializers import JournalSerializer


class JournalViewSet(ListCreateAPIViewSet):
    """
    create:

    Создание записи в журнале.

    ---

    ## Входные данные:
        {
          "child": "1",
          "time": "10:30",
          "action": "1",  // Событие: ребенка привели - 1, забрали - 2
          "parent": "1",
          "date": "2012-02-02"
        }
    """
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    filter_class = JournalFilterSet
