from rest_framework.viewsets import ModelViewSet

from apps.child.models import Child, Parent
from api.v1.child.serializers import ChildSerializer, ParentSerializer


class ChildViewSet(ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
    filter_fields = ['is_studying']


class ParentViewSet(ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
