from apps.child.models import Child, Parent

from api.common import CreateUpdateAPIViewSet, ListCreateAPIViewSet
from api.v1.child.serializers import ChildSerializer, ParentSerializer


class ChildViewSet(CreateUpdateAPIViewSet):
    """
    create:

    Создание детей.

    ---

    ## Входные данные:
        {
          "first_name": "Иван",
          "last_name": "Попов",
          "gender": "1",  // Пол ребенка: 1 - Мужской, 2 - Женский
          "grade": 2,  // Класс ребенка
          "photo": "data:image/gif;base64,R0lGODlh...",  // Фото в формате base64
          "is_studying": true,
          "parents": [1, 2],  // Идентификаторы родителей ребенка
          "date_of_birth": "2005-12-22"
        }
    """
    queryset = Child.objects.all()
    serializer_class = ChildSerializer


class ParentViewSet(ListCreateAPIViewSet):
    """
    create:

    Создание родителей.

    ---

    ## Входные данные:
        {
          "first_name": "Иван",
          "last_name": "Попов",
        }
    """
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
