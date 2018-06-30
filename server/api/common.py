from rest_framework.mixins import UpdateModelMixin, CreateModelMixin
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import GenericViewSet


class CreateUpdateAPIViewSet(CreateModelMixin,
                             UpdateModelMixin,
                             GenericViewSet):

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ListCreateAPIViewSet(GenericViewSet,
                           ListCreateAPIView):
    pass
